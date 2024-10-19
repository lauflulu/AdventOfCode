#pragma once
#include <Arduino.h>

class Pair
{
public:
    Pair(String input);

    bool is_fully_contained();
    bool is_overlapping();

private:
    uint8_t _elf_1_low;
    uint8_t _elf_1_high;
    uint8_t _elf_2_low;
    uint8_t _elf_2_high;
};