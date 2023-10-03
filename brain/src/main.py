import time
import serial

from devices.conveyor import ConveyorBelt


def main():
    conveyor_serial = serial.Serial("COM3", 9600)

    print("Initializing robotic interface...\n")
    time.sleep(3)
    
    cb = ConveyorBelt(conveyor_serial)
    while True:
        cb.toggle(run=True)

if __name__ == "__main__":
    main()