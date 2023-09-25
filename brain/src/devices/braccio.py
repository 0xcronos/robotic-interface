from serial import Serial

from devices.arduino import Arduino


class BraccioArm(Arduino):
    def __init__(self, serial_port: Serial) -> None:
        super(BraccioArm, self).__init__(serial_port)