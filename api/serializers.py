from rest_framework import serializers
from .models import User, Place, Visit

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'userName', 'userEmail', 'userContact', 'userRole')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('placeID', 'placeName')

class VisitSerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'tagID', 'datetime', 'duration')