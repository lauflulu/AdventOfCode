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

    uint32_t get_score_1(void);
    uint32_t get_score_2(void);
    void poll(void);

private:
    void update_score_1(String &message);
    void update_score_2(String &message);

private:
    uint32_t score_1{};
    uint32_t score_2{};
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

    Game score_map_2[9] = {
        {"A X", 0 + 3},
        {"A Y", 3 + 1},
        {"A Z", 6 + 2},
        {"B X", 0 + 1},
        {"B Y", 3 + 2},
        {"B Z", 6 + 3},
        {"C X", 0 + 2},
        {"C Y", 3 + 3},
        {"C Z", 6 + 1}};
};
