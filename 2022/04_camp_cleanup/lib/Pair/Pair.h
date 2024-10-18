#pragma once
#include <Arduino.h>

class Pair
{
public:
    Pair(String input) : _input{input} {}

    bool is_fully_contained();

private:
    String _input;
};