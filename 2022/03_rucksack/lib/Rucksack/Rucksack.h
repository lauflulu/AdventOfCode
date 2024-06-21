#pragma once

#include <Arduino.h>

class Rucksack
{
public:
    Rucksack(String contents);

    uint8_t compute_priority();

private:
    void split_compartments();
    char find_duplicate();

private:
    String _contents;
    String _left_compartment;
    String _right_compartment;
};