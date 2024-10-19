#include <Arduino.h>
#include <Pair.h>

uint32_t line_count{0U};
uint32_t contained_count{0U};
uint32_t overlap_count{0U};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  String input = Serial.readStringUntil(0x0A);
  line_count++;

  Pair pair{input};
  bool is_contained = pair.is_fully_contained();
  contained_count += is_contained;
  bool is_overlapping = pair.is_overlapping();
  overlap_count += is_overlapping;

  String response = String("line: ") + line_count + String(", contained: ") + contained_count + String(", overlapping: ") + overlap_count;
  Serial.println(response);
}