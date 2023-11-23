from enum import Enum
from serial import Serial

from devices.device import Device


class ActionState(Enum):
    PICKUP = 'pickUp\n'
    
    
class BraccioArm(Device):
    def __init__(self, serial_port: str, baudrate: int) -> None:
        super(BraccioArm, self).__init__(serial_port, baudrate)
        self.is_picking_up = False
    
    def pickUp(self) -> None:
        self.is_picking_up = True
        print("Picking up object...")
        
        self.write(ActionState.PICKUP.value)
        self.__update_status()

        print("Picking up object...: Done")
    
    def __update_status(self) -> None:
        response = self.read()
        if response == "done pickup":
            self.is_picking_up = False