from serial import Serial

from brain.src.devices.device import Device


class BraccioArm(Device):
    def __init__(self, serial_port: Serial) -> None:
        super(BraccioArm, self).__init__(serial_port)
    
    def move(angles: list) -> None:
        pass