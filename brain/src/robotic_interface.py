from devices.device import Device
from object_detector.recyclable_object_detector import RecyclableObjectDetector


class RoboticInterface:
    def __init__(self, 
        conveyor_belt: Device, 
        braccio_arm: Device,
        proximity_sensor: Device,
        object_detector: RecyclableObjectDetector
    ) -> None:
        self.conveyor_belt = conveyor_belt
        self.braccio_arm = braccio_arm
        self.proximity_sensor = proximity_sensor
        self.object_detector = object_detector

    def update_current_distance(self) -> None:
        while True:
            self.proximity_sensor.read_distance()
            
    def detect_recyclable_object(self) -> None:
        self.object_detector.execute()

    def recycle(self) -> None:
        self.conveyor_belt.toggle(run=True)

        while True:
            if self._is_available_for_pickup():
                is_pickup_done = self.braccio_arm.pick_up()
                
                if is_pickup_done == True:
                    self.object_detector.is_cardboard = False

    def _is_available_for_pickup(self) -> bool:
        return (
            self.object_detector.is_cardboard
            and (8 > self.proximity_sensor.current_distance > 0)
            and not self.braccio_arm.is_picking_up
        )
        
