from enum import Enum

from devices.device import Device


class ActionState(Enum):
    PICKUP = 'pickUp\n'
    
    
class BraccioArm(Device):
    def __init__(self, serial_port: str, baudrate: int) -> None:
        super(BraccioArm, self).__init__(serial_port, baudrate)
        self.is_picking_up = False
    
    # Returns False if task done otherwise returns True
    def pick_up(self) -> bool:
        if not self.is_picking_up:
            print("Picking up object...")
            self.is_picking_up = True
            self.write(ActionState.PICKUP.value)

        response = self.read()
        
        if response == "done pickup":
            self.is_picking_up = False
            print("Picking up object...: Done")
            return True
        
        return False