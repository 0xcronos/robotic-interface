#include <AccelStepper.h>

// Definitions for the ULN2003 driver
#define MotorInterfaceType 4
#define IN1 8
#define IN2 9
#define IN3 10
#define IN4 11


AccelStepper stepper(MotorInterfaceType, 8, 10, 9, 11);

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }

  stepper.setMaxSpeed(450);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    switch (command) {
      case 'r':
        stepper.setSpeed(450);
        Serial.println("the conveyor belt is now running");
        break;
      case 's':
        stepper.setSpeed(0);
        Serial.println("the conveyor belt is now stopped");
        break;
      default:
        Serial.println("Invalid command.");
        Serial.println(command);
        break;
    }
  }
  stepper.runSpeed();
}
