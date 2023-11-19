from serial import Serial


class Device:
    def __init__(self, serial_port: Serial) -> None:
        self.serial_port = serial_port
    
    def write(self, value: str) -> None:
        encoded_value = self.__encode(value)
        self.serial_port.write(encoded_value)

    
    def read(self) -> str:
        response = self.serial_port.readline()
        response = self.__decode(response)
        return response


    def __encode(self, value: str) -> bytearray:
        return bytearray(value.encode('utf-8'))
    
    def __decode(self, value: bytearray) -> str:
        return value.decode('utf-8').replace('\n', '').replace('\r', '') 
