#include <Arduino.h>
#include <SPIFFS.h>
#include <Stacks.h>

void setup()
{
  Serial.begin(115200);
  SPIFFS.begin(true);

  File file = SPIFFS.open("/initial_stacks.txt", "r");
  String input_stacks;

  while (file.available())
  {
    char next_char = file.read();
    input_stacks += next_char;
  }

  file.close();

  Stacks<9, 56> stacks{input_stacks};

  Serial.println("hello");
  String buffer{""};
  Serial.println(stacks.to_string(buffer));
}

void loop()
{
}