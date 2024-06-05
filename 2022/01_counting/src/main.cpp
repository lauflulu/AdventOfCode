#include <main.h>

SerialAdapter serial_adapter{Serial};
Counter counter{serial_adapter};
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    counter.poll();
    Serial.println(counter.get_highest_count());
}
