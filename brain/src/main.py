import threading

from devices.conveyor import ConveyorBelt
from devices.proximity_sensor import ProximitySensor
from devices.braccio import BraccioArm


conveyor_belt = ConveyorBelt("/dev/cu.usbserial-10", 9600)
braccio_arm = BraccioArm("/dev/cu.usbserial-1120", 9600)
proximity_sensor = ProximitySensor("/dev/cu.usbserial-1130", 115200)

def update_current_distance():
    while True:
        current_distance = proximity_sensor.read_distance()
        print(current_distance)

def main():
    conveyor_belt.toggle(run=True)
    
    while True:
        if (8 > proximity_sensor.current_distance > 0) and not braccio_arm.is_picking_up:
            braccio_arm.pickUp()


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    proximity_sensor_thread = threading.Thread(target=update_current_distance)
    
    main_thread.start()
    proximity_sensor_thread.start()