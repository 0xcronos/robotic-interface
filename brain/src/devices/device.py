import time
from serial import Serial


class Device:
    def __init__(self, serial_port: str, baudrate: int) -> None:
        self.serial = self.__create_serial(serial_port, baudrate)
    
    def write(self, value: str) -> None:
        encoded_value = self.__encode(value)
        self.serial.write(encoded_value)

    def read(self) -> str:
        response = self.serial.readline()
        response = self.__decode(response)
        return response

    def __create_serial(self, serial_port: str, baudrate: int) -> Serial:
        serial = Serial(serial_port, baudrate)
        print(f"Initializing device at port {serial_port}...")
        time.sleep(3)
        print(f"Initializing device at port {serial_port}...: Done")
        return serial

    def __encode(self, value: str) -> bytearray:
        return bytearray(value.encode('utf-8'))
    
    def __decode(self, value: bytearray) -> str:
        return value.decode('utf-8').replace('\n', '').replace('\r', '') 
