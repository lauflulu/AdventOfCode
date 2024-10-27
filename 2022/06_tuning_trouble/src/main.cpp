#include <Arduino.h>

uint16_t packet_count{0U};

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  String input = Serial.readStringUntil(0x0A);
  packet_count++;

  String response = String("packet: ") + packet_count;
  Serial.println(response);
}