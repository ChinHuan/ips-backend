from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from django.utils.dateparse import parse_duration

from .serializers import UserSerializer, PlaceSerializer, VisitPlaceSerializer, VisitSerializer, CoordinateSerializer
from .models import User, Place, Visit, Coordinate

class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request, userEmail):
        try:
            user = User.objects.get(userEmail=userEmail)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(None)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitListView(ListCreateAPIView, UpdateModelMixin):
    serializer_class = VisitPlaceSerializer

    def filter_queryset(self, queryset):
        visits = queryset.filter(user=self.kwargs['userID'])
        return visits

    def get_queryset(self):
        queryset = self.filter_queryset(Visit.objects.all())
        return queryset

    def post(self, request):
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, userID):
        try:
            Visit.objects.filter(user=userID).update(duration=parse_duration(request.data['duration']))
        except:
            return Response("An error occurred", status=status.HTTP_400_BAD_REQUEST)
        return Response("Updated successfully", status=status.HTTP_200_OK)

class CoordinateView(RetrieveAPIView):
    serializer_class = CoordinateSerializer

    def get(self, request, tagID):
        try:
            coordinate = Coordinate.objects.filter(tagID=tagID).order_by('datetime').last()
            return Response(CoordinateSerializer(coordinate).data)
        except Coordinate.DoesNotExist:
            return Response(None)
