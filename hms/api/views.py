import time
import random
import json
import asyncio
from aiocoap import *
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse

from .models import *

from . import fetch_data

def index(request):
    return HttpResponse("SolarFi Hub Management System API endpoints.")

def battery(request):
    if request.method == 'GET':
        data = fetch_data.get_all()
        b1 = data[0]
        print(b1)
        if len(data) == 2:
            b2 = data[1]
        b2 = None
        context = {
            'b1': b1,
            'b2': b2
            }
        return render(request, 'battery1.htm', context)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        b = Battery(**data)
        b.save()
        return HttpResponse(str(b.__dict__))