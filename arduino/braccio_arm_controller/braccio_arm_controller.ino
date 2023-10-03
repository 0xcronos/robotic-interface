#include <BraccioRobot.h>
#include <Servo.h>

Position armPosition;

void setup()
{
    Serial.begin(9600);

    while (!Serial) { ; }
    BraccioRobot.init();
}

// base degrees           : from 0 to 180 degrees
// shoulder degrees       : from 15 to 165 degrees
// elbow degrees          : from 0 to 180 degrees
// wrist degrees          : from 0 to 180 degrees
// wrist rotation degrees : from 0 to 180 degrees
// gripper degrees        : from 10 to 73 degrees (10 open, 73 closed)
void loop()
{
    if (Serial.available())
    {
        String command = Serial.readStringUntil('\n');

        command.trim();

        if (command.startsWith("angles:"))
        {
            Serial.println(command);
            String angles = command.substring(command.indexOf(":") + 1, (command.length()));
            int speed = 150;
            armPosition.setFromString(angles);

            BraccioRobot.moveToPosition(armPosition, speed);
        }
        else
        {
            Serial.println("Invalid syntax for specified command.");
        }
    }
}