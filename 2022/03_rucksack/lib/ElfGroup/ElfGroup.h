#pragma once

#include <Arduino.h>

class ElfGroup
{
public:
    ElfGroup(){};

    void add(String contents);
    uint8_t compute_priority();

private:
    char find_common_item();

private:
    String _contents[3];
};