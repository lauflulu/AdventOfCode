#include <main.h>

uint32_t sum{0U};
uint16_t line_count{0U};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  String contents = Serial.readStringUntil(0x0A);
  Rucksack rucksack{contents};
  sum += rucksack.compute_priority();
  line_count++;
  Serial.println(line_count + String(",") + contents + String(",") + sum);
}
