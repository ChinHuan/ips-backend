from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from django.utils.dateparse import parse_duration

from .serializers import UserSerializer, PlaceSerializer, VisitPlaceSerializer, VisitSerializer, CoordinateSerializer, TagSerializer, ContactSerializer, NotificationSerializer
from .models import User, Place, Visit, Coordinate, Tag, Contact, TagToToken

import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("api/static/ips-fcm-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)


class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request, userEmail):
        """
        Get a user given a user email.
        :param request: The request object posted by the caller
        :param userEmail: The parameter given by the caller
        :return: User object if it exists else None
        """
        try:
            user = User.objects.get(userEmail=userEmail)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(None)

    def post(self, request):
        """
        Post a user.
        :param request: The request object posted by the caller
        :return: User object with the appropriate status code
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitListView(ListCreateAPIView, UpdateModelMixin):
    serializer_class = VisitPlaceSerializer

    def filter_queryset(self, queryset):
        """
        Filter a queryset based on user ID.
        :param queryset: The queryset to be filtered
        :return: The filtered queryset
        """
        visits = queryset.filter(user=self.kwargs['userID'])
        return visits

    def get_queryset(self):
        """
        Get a list of visits of a user.
        :return: A list of visists of a user
        """
        queryset = self.filter_queryset(Visit.objects.all())
        return queryset

    def post(self, request):
        """
        Post a visit record.
        :param request: The request object posted by the caller
        :return: Visit object with the appropriate status code
        """
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, userID):
        """
        Update the visit duration.
        :param request: The request object posted by the caller
        :param userID: The visit of the user to be updated
        :return: The appropriate status code
        """
        try:
            Visit.objects.filter(user=userID).update(duration=parse_duration(request.data['duration']))
        except:
            return Response("An error occurred", status=status.HTTP_400_BAD_REQUEST)
        return Response("Updated successfully", status=status.HTTP_200_OK)

class CoordinateView(RetrieveAPIView):
    serializer_class = CoordinateSerializer

    def get(self, request, tagID):
        """
        Get the coordinate of a tag.
        :param request: The request object posted by the caller
        :param tagID: The parameter given by the caller
        :return: Coordinate object if it exists else None
        """
        try:
            coordinate = Coordinate.objects.filter(tag=tagID).order_by('datetime').last()
            return Response(CoordinateSerializer(coordinate).data)
        except Coordinate.DoesNotExist:
            return Response(None)

    def post(self, request):
        """
        Post multiple coordinate records.
        :param request: The request object posted by the caller
        :return: The appropriate status code
        """
        try:
            Coordinate.objects.bulk_create([Coordinate(
                tag = Tag.objects.get(tagID = c['tag']),
                place = Place.objects.get(placeID = c['place']),
                x = c['x'],
                y = c['y'],
                inCloseContact = c['inCloseContact']
            ) for c in request.data])
            return Response("Added successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class CoordinatesView(ListAPIView):
    serializer_class = CoordinateSerializer

    def filter_queryset(self, queryset):
        """
        Filter a queryset based on place ID.
        :param queryset: The queryset to be filtered
        :return: The filtered queryset
        """
        coordinates = queryset.filter(place=self.kwargs['placeID'])
        coordinates = coordinates.filter(datetime__gt=datetime.utcnow() - timedelta(seconds=30))
        return coordinates

    def get_queryset(self):
        """
        Get a list of coordinates in a place.
        :return: A list of coordinates in a place
        """
        queryset = self.filter_queryset(Coordinate.objects.all())
        return queryset

class ContactView(RetrieveAPIView):
    serializer_class = ContactSerializer

    def post(self, request):
        """
        Post multiple contact records.
        Push notifications if required.
        :param request: The request object posted by the caller
        :return: The appropriate status code
        """
        try:
            Contact.objects.bulk_create([Contact(
                datetime = c['datetime'],
                tag = Tag.objects.get(tagID = c['tag']),
                place = Place.objects.get(placeID = c['place'])
            ) for c in request.data])

            for c in request.data:
                try:
                    tagToToken = TagToToken.objects.get(tag=c['tag'])
                    token = tagToToken.token
                    message = messaging.Message(
                        notification=messaging.Notification(
                            title = "Warning!",
                            body = "You are in close distance with others."
                        ),
                        token=token,
                    )
                    response = messaging.send(message)
                    print(response)
                except TagToToken.DoesNotExist:
                    print("Token does not exist")
                    pass
            return Response("Added successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class NotificationView(RetrieveAPIView):
    serializer_class = NotificationSerializer

    def post(self, request):
        """
        Either subscribe or unsubscribe for a notification
        :param request: The request object posted by the caller
        :return: The appropriate status code
        """
        token = request.data['accessToken']
        tag = request.data['tag']
        mode = request.data['mode']
        if mode == 'subscribe':
            try:
                TagToToken.objects.get(tag=tag)
                TagToToken.objects.filter(tag=tag).update(token=token)
            except TagToToken.DoesNotExist:
                tagToToken = TagToToken(
                    tag=Tag.objects.get(tagID=tag),
                    token=token
                )
                tagToToken.save()
            return Response("Subscribed successfully", status=status.HTTP_201_CREATED)
        elif mode == 'unsubscribe':
            TagToToken.objects.filter(tag=tag).delete()
            return Response("Unsubscribed successfully", status=status.HTTP_201_CREATED)
