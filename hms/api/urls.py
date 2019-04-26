from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('battery', views.battery, name='battery'),
    path('locker', views.locker, name='locker'),
    path('network', views.network, name='network'),
    path('amenities', views.amenities, name='amenities'),
    path('help', views.help, name='help'),
    path('b', views.battery_json),
    path('n', views.network_json),
    path('l', views.locker_json),
    path('a', views.amenities_json),
    path('getbattery', views.getBattery)
]