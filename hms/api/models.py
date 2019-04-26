from django.db import models

# Create your models here.
class Battery(models.Model):
    device_id = models.PositiveSmallIntegerField(default=0)
    capacity = models.PositiveSmallIntegerField(default=0)
    percentage = models.PositiveSmallIntegerField(default=0)
    is_charging = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    temp = models.SmallIntegerField(default=0)     
    e_in = models.PositiveSmallIntegerField(default=0)
    e_out = models.PositiveSmallIntegerField(default=0)
    p_in = models.PositiveSmallIntegerField(default=0)
    p_out = models.PositiveSmallIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class Network(models.Model):
    is_connected = models.BooleanField(default=False)
    is_modem_on = models.BooleanField(default=False)
    bandwidth = models.PositiveIntegerField(default=0)
    bandwidth_usage = models.PositiveIntegerField(default=0)
    modem_web_interface = models.TextField()
    is_router_on = models.BooleanField(default=False)
    num_device = models.PositiveSmallIntegerField(default=0)
    router_web_interface = models.TextField(default='./')
    timestamp = models.DateTimeField(auto_now_add=True)

class Locker(models.Model):
    num_lockers = models.PositiveSmallIntegerField(default=0)
    num_charging = models.PositiveSmallIntegerField(default=0)
    num_charged = models.PositiveSmallIntegerField(default=0)
    energy_used = models.PositiveSmallIntegerField(default=0)
    web_interface = models.TextField(default='./')
    timestamp = models.DateTimeField(auto_now_add=True)

class Amenities(models.Model):
    kiosk_temp = models.SmallIntegerField(default=0)
    locker_lights = models.BooleanField(default=False)
    locker_lights_p = models.PositiveSmallIntegerField(default=0)
    kiosk_lights = models.BooleanField(default=False)
    kiosk_lights_p = models.PositiveSmallIntegerField(default=0)
    mini_fridge = models.BooleanField(default=False)
    mini_fridge_p = models.PositiveSmallIntegerField(default=0)
    coffee_machine = models.BooleanField(default=False)
    coffee_machine_p = models.PositiveSmallIntegerField(default=0)
    blender = models.BooleanField(default=False)
    blender_p = models.PositiveSmallIntegerField(default=0)
    tv = models.BooleanField(default=False)
    tv_p = models.PositiveSmallIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)