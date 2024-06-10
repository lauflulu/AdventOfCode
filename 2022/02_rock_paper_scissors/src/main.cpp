#include <main.h>

SerialAdapter serial_adapter{Serial};
Score score{serial_adapter};
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  score.poll();
  Serial.println(String(score.get_total_score()));
}
