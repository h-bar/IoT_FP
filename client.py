import logging
import asyncio
import json
import requests

from aiocoap import *

async def main():
    protocol = await Context.create_client_context()
    # sock = protocol.request_interfaces[2].token_interface.message_interface.transport._RecvmsgSelectorDatagramTransport__sock # Oh lawd
    # sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 128)
    # interface_index = socket.if_nametoindex('eno1')
    # sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_IF, interface_index)
    
    # request = 
    request = Message(code=GET, uri='coap://224.0.1.187/.well-known/core', mtype=2)

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())