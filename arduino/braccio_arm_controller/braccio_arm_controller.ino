#include <BraccioRobot.h>
#include <Servo.h>

Position pos;

void setup() {
  Serial.begin(9600);

  while (!Serial) { ; }
  BraccioRobot.init();
}

int* parseAnglesString(String inputString, int numValues) {
  int* angles = new int[numValues];
  int index = 0;

  while (index < numValues) {
    int commaPosition = inputString.indexOf(',');

    if (commaPosition != -1) {
      String valueStr = inputString.substring(0, commaPosition);
      angles[index] = valueStr.toInt();
      inputString.remove(0, commaPosition + 1);
    } else {
      angles[index] = inputString.toInt();
      break;
    }
    index++;
  }

  return angles;
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command.startsWith("angles:")) {
      Serial.println(command);
      String rawAngles = command.substring(command.indexOf(":")+1, (command.length()));

      int* angles = parseAnglesString(rawAngles, 6);      
      // Set the position
      // M1=base degrees. Allowed values from 0 to 180 degrees
      // M2=shoulder degrees. Allowed values from 15 to 165 degrees (Checked)
      // M3=elbow degrees. Allowed values from 0 to 180 degrees (Checked)
      // M4=wrist degrees. Allowed values from 0 to 180 degrees (bug: 75 a 180)
      // M5=wrist rotation degrees. Allowed values from 0 to 180 degrees (Checked)
      // M6=gripper degrees. Allowed values from 10 to 73 degrees. 10: the toungue is open, 73: the gripper is closed. (Checked)
      pos.set(angles[0],  angles[1], angles[2], angles[3], angles[4],  angles[5]);

    BraccioRobot.moveToPosition(pos, 100);
    }
    else {
      Serial.println("Invalid syntax for specified command.");
    }
  }
}