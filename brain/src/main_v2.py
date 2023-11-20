import time
import serial
import threading

from devices.conveyor import ConveyorBelt
from devices.device import Device


current_distance = -1

if __name__ == "__main__":
    devices = []
    robotic_interface = RoboticInterface(devices, camera)
    robotic_interface.run()