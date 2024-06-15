#pragma once

#include <Arduino.h>
#include <SerialAdapter.h>

struct Game
{
    String outcome;
    uint8_t score;
};

class Score
{
public:
    Score(ISerial &serial_) : serial{serial_} { serial = serial_; };

    uint32_t get_total_score(void);
    void poll(void);

    void update_score_1(String &message);

private:
    uint32_t score_1{};
    ISerial &serial;

    Game score_map_1[9] = {
        {"A X", 4},
        {"A Y", 8},
        {"A Z", 3},
        {"B X", 1},
        {"B Y", 5},
        {"B Z", 9},
        {"C X", 7},
        {"C Y", 2},
        {"C Z", 6}};
};
