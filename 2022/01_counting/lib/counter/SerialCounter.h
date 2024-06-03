#include <Arduino.h>

class SerialCounter
{
public:
    SerialCounter(){};

    uint32_t get_highest_count(void);

private:
    uint32_t current_count{};
    uint32_t highest_count{};
};