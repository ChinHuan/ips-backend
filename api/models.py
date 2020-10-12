from django.db import models

class User(models.Model):
    class Role(models.IntegerChoices):
        USER = 1
        ADMIN = 2

    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=60)
    userEmail = models.CharField(max_length=60)
    userContact = models.CharField(max_length=20, null=True, blank=True)
    userRole = models.IntegerField(choices=Role.choices)
    userPhotoUrl = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.userID, self.userName)

class Place(models.Model):
    placeID = models.AutoField(primary_key=True)
    placeName = models.CharField(max_length=60)
    placePhotoUrl = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.placeID, self.placeName)

class Tag(models.Model):
    tagID = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return '{}'.format(self.tagID)

class Visit(models.Model):
    visitID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return '{} {} > {}'.format(self.datetime, self.user, self.place)

class Coordinate(models.Model):
    coordinateID = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    inCloseContact = models.BooleanField()

    def __str__(self):
        return '{} ({:.3f}, {:.3f}) {} {}'.format(self.tag, self.x, self.y, self.place, self.datetime)

class Contact(models.Model):
    contactID = models.AutoField(primary_key=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.tag, self.place, self.datetime)
