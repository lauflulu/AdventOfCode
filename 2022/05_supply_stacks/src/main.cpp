#include <Arduino.h>
#include <SPIFFS.h>

#include <GiantCargoDock.h>

GiantCargoDock stacks;

void setup()
{
  Serial.begin(115200);
  SPIFFS.begin(true);

  File file = SPIFFS.open("/initial_stacks.txt", "r");
  String input_text;

  while (file.available())
  {
    char next_char = file.read();
    input_text += next_char;
  }

  file.close();

  stacks.load(input_text);

  String buffer{""};
  stacks.read_top(buffer);
  Serial.println(buffer);
}

void loop()
{
}