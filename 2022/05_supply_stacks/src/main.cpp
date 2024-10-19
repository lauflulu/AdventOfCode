#include <Arduino.h>
#include <SPIFFS.h>
#include <Stacks.h>

void setup()
{
  Serial.begin(115200);
  SPIFFS.begin(true);
}

void loop()
{
  delay(1000);

  Serial.println("hello");
  Stacks stacks{};

  Serial.println(stacks._input_stacks);
}