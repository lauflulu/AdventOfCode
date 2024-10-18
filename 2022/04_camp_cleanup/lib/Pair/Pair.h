#pragma once
#include <Arduino.h>

class Pair
{
public:
    Pair(String input) { _parse_input(input); }

    bool is_fully_contained();

private:
    void _parse_input(String input);

private:
    uint8_t _elf_1_low;
    uint8_t _elf_1_high;
    uint8_t _elf_2_low;
    uint8_t _elf_2_high;
};