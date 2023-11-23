#include <BraccioRobot.h>
#include <Servo.h>
#define GRIPPER_HALF_CLOSED 64
#define GRIPPER_OPEN 0

Position initialPosition(174, 120, 40, 100, 90, GRIPPER_CLOSED);
Position pos;

void moveArm(int* angles) {
  pos.set(angles[0], angles[1], angles[2], angles[3], angles[4], angles[5]);
  BraccioRobot.moveToPosition(pos, 200);
}

void pickUp() {
  int sequence[][6] = {
    { 165, 120, 40, 100, 90, GRIPPER_OPEN },
    { 165, 87, 18, 145, 90, GRIPPER_OPEN },
    { 165, 87, 18, 145, 90, GRIPPER_HALF_CLOSED },
    { 165, 120, 30, 120, 90, GRIPPER_HALF_CLOSED },
    { 75, 120, 30, 120, 90, GRIPPER_HALF_CLOSED },
    { 85, 100, 20, 140, 90, GRIPPER_HALF_CLOSED },
    { 85, 100, 30, 120, 90, GRIPPER_OPEN },
    { 165, 120, 40, 100, 90, GRIPPER_OPEN }
  };

  int sequence_length = sizeof(sequence) / sizeof(sequence[0]);
  for (int i = 0; i < sequence_length; i++) {
    moveArm(sequence[i]);
  }
}

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }
  BraccioRobot.init(initialPosition);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "pickUp") {
      pickUp();
      Serial.println("done pickup");
    }
  }
}
