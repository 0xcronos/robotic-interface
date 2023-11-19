import time
import serial

from devices.conveyor import ConveyorBelt


def main():
    conveyor_serial = serial.Serial("/dev/cu.usbserial-10", 9600)

    print("Initializing robotic interface...\n")
    time.sleep(3)
    
    cb = ConveyorBelt(conveyor_serial)
    cb.toggle(run=False)
    
    while True:
        cb.toggle(run=True)
        time.sleep(1)
        cb.toggle(run=False)
        time.sleep(1)