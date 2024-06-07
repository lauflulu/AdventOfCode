#pragma once

#include <Arduino.h>
#include <SerialAdapter.h>

class Counter
{
public:
    Counter(ISerial &serial_) : serial(serial_) { serial = serial_; };

    uint32_t get_highest_count(void);
    uint32_t get_top3_count(void);
    void poll(void);

private:
    uint32_t current_count{};
    uint32_t top3_counts[3]{};
    ISerial &serial;
};