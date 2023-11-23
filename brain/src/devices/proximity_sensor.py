from devices.device import Device 


class ProximitySensor(Device):
    def __init__(self, serial_port: str, baudrate: int) -> None:
        super(ProximitySensor, self).__init__(serial_port, baudrate)
        self.current_distance = -1

    def read_distance(self) -> float:
        distance = float(self.read())
        self.current_distance = distance if distance != -1 else self.current_distance

        return self.current_distance
