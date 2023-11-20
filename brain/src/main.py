import time
import serial
import threading

from devices.conveyor import ConveyorBelt
from devices.device import Device


current_distance = -1


def update_current_distance():
    global current_distance

    proximity_sensor_serial = serial.Serial("/dev/cu.usbserial-1130", 115200)
    print("Initializing proximity sensor...")
    time.sleep(3)
    print("Initializing proximity sensor...: Done\n")
    
    proximity_sensor = Device(proximity_sensor_serial)
    
    while True:
        distance = float(proximity_sensor.read())
        current_distance = distance if distance != -1 else current_distance
        print(current_distance)
    

def main():
    global current_distance
    
    # Initialize Conveyor Belt
    conveyor_serial = serial.Serial("/dev/cu.usbserial-10", 9600)
    print("Initializing conveyor belt...")
    time.sleep(3)
    print("Initializing conveyor belt...: Done\n")
    conveyor_belt = ConveyorBelt(conveyor_serial)
    
    # Initialize Braccio Arm
    braccio_serial = serial.Serial("/dev/cu.usbserial-1120", 9600)
    print("Initializing braccio arm...")
    time.sleep(3)
    print("Initializing braccio arm...: Done\n")
    braccio_arm = Device(braccio_serial)
     
    conveyor_belt.toggle(run=True)
    
    is_picking_up = False
    while True:
        if 5 > current_distance > 0 and not is_picking_up:
            is_picking_up = True
            
            print("Picking up object...")
            braccio_arm.write("pickUp\n")
            response = braccio_arm.read()
            
            if response == "done pickup":
                is_picking_up = False
                
            print("Picking up object...: Done\n")


if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    proximity_sensor_thread = threading.Thread(target=update_current_distance)
    
    main_thread.start()
    proximity_sensor_thread.start()