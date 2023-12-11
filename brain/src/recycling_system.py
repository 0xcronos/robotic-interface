import threading

from envyaml import EnvYAML

from devices.conveyor import ConveyorBelt
from devices.proximity_sensor import ProximitySensor
from devices.braccio import BraccioArm

from object_detector.recyclable_object_detector import RecyclableObjectDetector

from robotic_interface import RoboticInterface


class RecyclingSystem:
    def __init__(self, config: EnvYAML) -> None:
        self.robotic_interface = self._set_robotic_interface(config)
        self._initialize_threads()
    
    def run(self) -> None:
        self.recycling_thread.start()
        self.proximity_sensor_thread.start()
        self.object_detector_thread.start()

    def _set_robotic_interface(self, config: EnvYAML) -> RoboticInterface:
        conveyor_belt = ConveyorBelt(config['conveyor_belt.serial_port'], config['conveyor_belt.baudrate'])
        braccio_arm = BraccioArm(config['braccio_arm.serial_port'], config['braccio_arm.baudrate'])
        proximity_sensor = ProximitySensor(config['proximity_sensor.serial_port'], config['proximity_sensor.baudrate'])
        object_detector = RecyclableObjectDetector(config['object_detector'])
        return RoboticInterface(conveyor_belt, braccio_arm, proximity_sensor, object_detector)
    
    def _initialize_threads(self) -> None:
        self.recycling_thread = threading.Thread(target=self.robotic_interface.recycle)
        self.proximity_sensor_thread = threading.Thread(target=self.robotic_interface.update_current_distance)
        self.object_detector_thread = threading.Thread(target=self.robotic_interface.detect_recyclable_object)
