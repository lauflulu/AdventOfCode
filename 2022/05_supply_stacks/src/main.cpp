#include <Arduino.h>
#include <SPIFFS.h>
#include <Stacks.h>

String input_stacks;

void setup()
{
  Serial.begin(115200);
  SPIFFS.begin(true);

  File file = SPIFFS.open("/initial_stacks.txt", "r");

  while (file.available())
  {
    char next_char = file.read();
    input_stacks += next_char;
  }

  file.close();

  Stacks stacks{input_stacks};
}

void loop()
{
  delay(1000);

  Serial.println("hello");

  Serial.println(stacks._input_stacks);
}