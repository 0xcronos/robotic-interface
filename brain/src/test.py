from envyaml import EnvYAML
from devices.conveyor import ConveyorBelt
from devices.braccio import BraccioArm


config = EnvYAML('config.yaml')

conveyor_belt = ConveyorBelt(config['conveyor_belt.serial_port'], config['conveyor_belt.baudrate'])
conveyor_belt.toggle(run=True)

#braccio_arm = BraccioArm(config['braccio_arm.serial_port'], config['braccio_arm.baudrate'])
#braccio_arm.pickUp()
