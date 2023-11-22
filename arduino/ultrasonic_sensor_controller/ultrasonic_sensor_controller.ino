#include <NewPing.h>

#define TRIGGER_PIN 25
#define ECHO_PIN 26
#define MAX_DISTANCE 50

float distance;

// Ultrasonic sensor
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(115200);
}

void loop() {
  distance = sonar.ping_cm();

  if (distance >= 400 || distance < 2) {
    Serial.println(-1);
  } else {
    Serial.println(distance);
  }

  delay(500);
}