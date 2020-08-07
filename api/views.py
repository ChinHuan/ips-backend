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

class VisitListView(ListAPIView):
    serializer_class = VisitSerializer

    def get_queryset(self):
        visits = Visit.objects.filter(user=self.kwargs['userID']).all()
        return visits
