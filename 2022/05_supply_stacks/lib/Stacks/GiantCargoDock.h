#pragma once
#include <Arduino.h>
#include <Stack.h>

class GiantCargoDock
{
public:
    GiantCargoDock() {};

    void load(const String &input_text);
    void push_row(const String &line);
    void read_top(String &buffer);
    void process(const String &instruction);

private:
    std::array<Stack, 3> stacks{};
};
