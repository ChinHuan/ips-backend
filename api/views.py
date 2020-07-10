from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, PlaceSerializer, VisitSerializer
from .models import User, Place, Visit

class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class UserView(APIView):
    def get(self, request, userID):
        user = User.objects.get(userID=userID)
        return Response(UserSerializer(user).data)

class VisitListView(ListAPIView):
    serializer_class = VisitSerializer

    def get_queryset(self):
        visits = Visit.objects.filter(user=self.kwargs['userID']).all()
        return visits
