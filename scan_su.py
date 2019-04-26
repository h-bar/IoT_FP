import socket
import sys
from time import sleep
from typing import cast

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


def on_service_state_change(
    zeroconf: Zeroconf, service_type: str, name: str, state_change: ServiceStateChange,
) -> None:
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            if info.properties:
                print(info.properties[b'ipv6'].decode('UTF-8'))

if __name__ == '__main__':
    zeroconf = Zeroconf()
    browser = ServiceBrowser(zeroconf, "_su._tcp.local.", handlers=[on_service_state_change])

    sleep(1)
    zeroconf.close()
