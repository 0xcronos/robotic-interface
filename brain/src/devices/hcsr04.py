from enum import Enum
from serial import Serial

from devices.device import Device 


class ProximitySensor(Device):
    def __init__(self, serial_port: Serial) -> None:
        super(ProximitySensor, self).__init__(serial_port)