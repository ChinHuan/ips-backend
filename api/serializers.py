from rest_framework import serializers
from .models import User, Place, Visit

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'userName', 'userEmail', 'userContact', 'userRole', 'userPhotoUrl')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('placeID', 'placeName')

class VisitPlaceSerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'tagID', 'datetime', 'duration')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'user', 'tagID', 'datetime', 'duration')