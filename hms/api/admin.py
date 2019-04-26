from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Battery)
admin.site.register(Network)
admin.site.register(Amenities)
admin.site.register(Locker)