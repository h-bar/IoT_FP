import datetime
import logging
import json
import random

import asyncio

import aiocoap.resource as resource
import aiocoap

logging.basicConfig(level=logging.INFO)

def readData():
    battery = {
        'device_id': 0,
        'capacity': 3000,
        'percentage': random.randrange(20, 100),
        'is_charging': True,
        'is_online': True,
        'temp' : random.randrange(90, 122),     
        'e_in' : random.randrange(0, 900),
        'e_out': random.randrange(0, 900),
        'p_in': random.randrange(0, 4000),
        'p_out': random.randrange(0, 4000)
    }

    payload = json.dumps(battery)
    payload = payload.encode(encoding='ASCII') + b'\n'
    return payload

def getProfile():
    resp = b'This is a hahaha\n'
    return resp

class DataResource(resource.Resource):
    async def render_get(self, request):
        payload = readData()
        return aiocoap.Message(code=aiocoap.CHANGED, payload=payload)

class ProfileResource(resource.Resource):
    async def render_get(self, request):
        payload = getProfile()
        return aiocoap.Message(code=aiocoap.CHANGED, payload=payload)

def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(('.well-known', 'core'), resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(('data',), DataResource())
    root.add_resource(('profile',), ProfileResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()