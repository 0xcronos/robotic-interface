from enum import Enum
from serial import Serial

from devices.arduino import Arduino


class ActionState(Enum):
    RUN = 'r'
    STOP = 's'


class ConveyorBelt(Arduino):
    def __init__(self, serial_port: Serial) -> None:
        super(ConveyorBelt, self).__init__(serial_port)
        self.is_running = False
    
    def toggle(self, run: bool) -> bool:
        if run == self.is_running:
            print(f"the conveyor belt is already {'running' if run else 'stopped'}")
            return False
        
        action = ActionState.RUN.value if run else ActionState.STOP.value

        expected_response = f"the conveyor belt is now {'running' if run else 'stopped'}"

        action_done = self.do_action(action, expected_response)
        if not action_done:
            print(f"error while trying to {'run' if run else 'stop'} the conveyor belt")
            return False

        self.is_running = run

        return True
 