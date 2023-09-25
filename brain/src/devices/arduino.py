from serial import Serial


class ActionException(Exception):
    pass


class Arduino:
    def __init__(self, serial_port: Serial) -> None:
        self.serial_port = serial_port
    
    def do_action(self, action: str, expected_response: str) -> bool:
        encoded_action = self.__encode(action)
        self.serial_port.write(encoded_action)

        response = self.__read_from_serial() 
        if response != expected_response:
            raise ActionException("Error performing the action.\nError:", response)
        return True
    
    def __encode(self, val: str) -> bytearray:
        return bytearray(val.encode('utf-8'))
    
    def __read_from_serial(self) -> str:
        response = self.serial_port.readline()
        return response.decode('utf-8').replace('\n', '').replace('\r', '')
