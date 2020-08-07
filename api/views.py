from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from django.utils.dateparse import parse_duration

from .serializers import UserSerializer, PlaceSerializer, VisitPlaceSerializer, VisitSerializer
from .models import User, Place, Visit

class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class UserView(RetrieveAPIView):
    def get(self, request, userID):
        user = User.objects.get(userID=userID)
        return Response(UserSerializer(user).data)

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
