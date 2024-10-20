#pragma once
#include <Arduino.h>

class Stacks
{
public:
    Stacks(const String &input_stacks) : _input_stacks{input_stacks} {}

public:
    String _input_stacks;
};
