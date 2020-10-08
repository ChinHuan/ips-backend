from rest_framework import serializers
from .models import User, Place, Visit, Coordinate

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'userName', 'userEmail', 'userContact', 'userRole', 'userPhotoUrl')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('placeID', 'placeName', 'placePhotoUrl')

class VisitPlaceSerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'tagID', 'datetime', 'duration')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'user', 'tagID', 'datetime', 'duration')

class CoordinateSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Coordinate
        fields = ('coordinateID', 'tagID', 'datetime', 'place', 'x', 'y')