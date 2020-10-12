from rest_framework import serializers
from .models import User, Place, Visit, Coordinate, Tag, Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'userName', 'userEmail', 'userContact', 'userRole', 'userPhotoUrl')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('placeID', 'placeName', 'placePhotoUrl')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, obj):
        return obj.tagID

    class Meta:
        model = Tag
        fields = ('tagID',)

class VisitPlaceSerializer(serializers.HyperlinkedModelSerializer):
    place = PlaceSerializer()
    tag = TagSerializer()

    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'tag', 'datetime', 'duration')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visitID', 'place', 'user', 'tag', 'datetime', 'duration')

class CoordinateSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Coordinate
        fields = ('coordinateID', 'tag', 'datetime', 'place', 'x', 'y', 'inCloseContact')

class ContactSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Coordinate
        fields = ('contactID', 'place', 'datetime', 'tag')

class NotificationSerializer(serializers.Serializer):
    accessToken = serializers.CharField(max_length=200)
    tag = serializers.CharField(max_length=20)
    mode = serializers.CharField(max_length=20)