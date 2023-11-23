import threading

from devices.conveyor import ConveyorBelt
from devices.proximity_sensor import ProximitySensor
from devices.braccio import BraccioArm

from object_detector.recyclable_object_detector import RecyclableObjectDetector


conveyor_belt = ConveyorBelt("/dev/cu.usbserial-10", 9600)
braccio_arm = BraccioArm("/dev/cu.usbserial-1120", 9600)
proximity_sensor = ProximitySensor("/dev/cu.usbserial-1130", 115200)
model = RecyclableObjectDetector(path="object_detector/best.pt")

def detect_recyclable_object():
    config = {"source": 0, "device":'cpu'}
    model.execute(config)


def update_current_distance():
    while True:
        current_distance = proximity_sensor.read_distance()
        print(current_distance)


def main():
    conveyor_belt.toggle(run=True)
    
    while True:
        if model.is_carboard == "isCARBOARD" and (8 > proximity_sensor.current_distance > 0) and not braccio_arm.is_picking_up:
            is_picking_up = braccio_arm.pickUp()
            
            if is_picking_up == False:
                model.is_carboard = "isNotCARBOARD"


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    proximity_sensor_thread = threading.Thread(target=update_current_distance)
    object_detector_thread = threading.Thread(target=detect_recyclable_object)
    
    main_thread.start()
    proximity_sensor_thread.start()
    object_detector_thread.start()