#pragma once
#include <Arduino.h>
#include <Stack.h>

class GiantCargoDock
{
public:
    GiantCargoDock() {};
    GiantCargoDock(const String &input_stacks);

    void push_row(const String &line);
    void read_top(String &buffer);

    void process_instruction(const String &instruction)
    {
    }

public:
    std::array<Stack, 3> stacks{};
};
