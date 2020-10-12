from django.contrib import admin
from .models import User, Place, Visit, Coordinate, Tag, Contact

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Visit)
admin.site.register(Tag)
admin.site.register(Coordinate)
admin.site.register(Contact)