import time
from serial import Serial


class Device:
    def __init__(self, serial_port: str, baudrate: int) -> None:
        self.serial = self._create_serial(serial_port, baudrate)
    
    def write(self, value: str) -> None:
        encoded_value = self._encode(value)
        self.serial.write(encoded_value)

    def read(self) -> str:
        response = self.serial.readline()
        response = self._decode(response)
        return response

    def _create_serial(self, serial_port: str, baudrate: int) -> Serial:
        serial = Serial(serial_port, baudrate)
        print(f"Initializing device at port {serial_port}...")
        time.sleep(3)
        print(f"Initializing device at port {serial_port}...: Done\n")
        return serial

    def _encode(self, value: str) -> bytearray:
        return bytearray(value.encode('utf-8'))
    
    def _decode(self, value: bytearray) -> str:
        return value.decode('utf-8').replace('\n', '').replace('\r', '') 
