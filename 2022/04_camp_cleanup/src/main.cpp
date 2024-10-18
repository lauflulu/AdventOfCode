#include <Arduino.h>
#include <Pair.h>

uint32_t line_count{0U};
uint32_t result_count{0U};

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
  result_count += is_contained;
  String response = pair.is_fully_contained() ? String(", fully contained,") : String(", seperate,");

  Serial.println(line_count + response + result_count);
}