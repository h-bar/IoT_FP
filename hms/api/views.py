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

def index(request):
    return HttpResponse("SolarFi Hub Management System API endpoints.")

def battery(request):
    if request.method == 'GET':
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_event_loop()
        resp = loop.run_until_complete(requestData('127.0.0.1', 'data'))
        loop.close()

        b = Battery.objects.latest('timestamp')
        b0 = Battery.objects.filter(device_id=0).latest('timestamp')
        b1 = Battery.objects.filter(device_id=0).latest('timestamp')
        context = {
            'b': b,
            'b0': b0,
            'b1': b1
            }
        return render(request, 'battery1.htm', context)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        b = Battery(**data)
        b.save()
        return HttpResponse(str(b.__dict__))

def network(request):
    if request.method == 'GET':
        n = Network.objects.latest('timestamp')
        context = {'n': n}
        return render(request, 'network1.htm', context)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        n = Network(**data)
        n.save()
        return HttpResponse(str(n.__dict__))

def locker(request):
    if request.method == 'GET':
        l = Locker.objects.latest('timestamp')
        context = {'l': l}
        return render(request, 'locker1.htm', context)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        l = Locker(**data)
        l.save()
        return HttpResponse(str(l.__dict__))

def amenities(request):
    if request.method == 'GET':
        a = Amenities.objects.latest('timestamp')
        context = {'a': a}
        return render(request, 'amenities1.htm', context)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        a = Amenities(**data)
        a.save()
        return HttpResponse(str(a.__dict__))

def help(request):
    return render(request, 'help1.htm')


def battery_json(request):
    b = Battery.objects.latest('timestamp').__dict__
    del b['_state']
    return JsonResponse(b)

def network_json(request):
    n = Network.objects.latest('timestamp').__dict__
    return HttpResponse(str(n))

def locker_json(request):
    l = Locker.objects.latest('timestamp').__dict__
    return HttpResponse(str(l))

def amenities_json(request):
    a = Amenities.objects.latest('timestamp').__dict__
    return HttpResponse(str(a))

def getBattery(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    resp = loop.run_until_complete(requestData('127.0.0.1', 'data'))
    loop.close()
    return HttpResponse(str(resp))

async def requestData(hostname, endpoint):
    uri = 'coap://'+ hostname + '/' + endpoint
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri=uri)

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
        return e
    else:
        data = json.loads(response.payload)
        b = Battery(**data)
        b.save()
        return data
    