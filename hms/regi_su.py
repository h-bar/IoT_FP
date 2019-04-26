import logging
import socket
import sys
import netifaces
from time import sleep

from zeroconf import ServiceInfo, Zeroconf


logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    info = netifaces.ifaddresses('wlp2s0')[netifaces.AF_INET]
    info6 = netifaces.ifaddresses('wlp2s0')[netifaces.AF_INET6]
    print(info6[0]['addr'])

    desc = {
        'name': 'su-0',
        'ipv6': info6[0]['addr']
    }

    info = ServiceInfo("_su._tcp.local.",
                       "su-0._su._tcp.local.",
                       socket.inet_aton(info[0]['addr']), 80, 0, 0,
                       desc, "su-0.local.")

    zeroconf = Zeroconf()
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(info)
        zeroconf.close()
