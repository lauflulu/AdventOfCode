#include <main.h>

uint32_t sum{0U};
uint32_t sum_of_priorities_2{0U};
uint16_t line_count{0U};
ElfGroup current_group{};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  String contents = Serial.readStringUntil(0x0A);
  Rucksack rucksack{contents};
  current_group.add(contents);
  sum += rucksack.compute_priority();
  sum_of_priorities_2 += current_group.compute_priority();
  line_count++;
  Serial.println(line_count + String(",") + sum + String(",") + sum_of_priorities_2);
}
