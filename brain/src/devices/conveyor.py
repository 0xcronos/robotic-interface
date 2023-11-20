from enum import Enum
from serial import Serial

from devices.device import Device 


class ActionState(Enum):
    RUN = 'r'
    STOP = 's'


class ConveyorBelt(Device):
    def __init__(self, serial_port: Serial) -> None:
        super(ConveyorBelt, self).__init__(serial_port)
        self.is_running = False
    
    def toggle(self, run: bool) -> bool:
        if run == self.is_running:
            return False
        
        action = ActionState.RUN.value if run else ActionState.STOP.value

        self.write(action)
        self.is_running = run

        return True
 