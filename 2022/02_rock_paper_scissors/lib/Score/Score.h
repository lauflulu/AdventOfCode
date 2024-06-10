#pragma once

#include <Arduino.h>
#include <SerialAdapter.h>

class Score
{
public:
    Score(ISerial &serial_) : serial{serial_} { serial = serial_; };

    uint32_t get_total_score(void);
    void poll(void);

private:
    uint32_t score{};
    ISerial &serial;
};