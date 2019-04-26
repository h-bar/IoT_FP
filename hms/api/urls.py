from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('battery', views.battery, name='battery'),
]