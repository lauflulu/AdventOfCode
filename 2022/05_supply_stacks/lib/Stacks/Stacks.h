#pragma once
#include <Arduino.h>
#include <SPIFFS.h>

class Stacks
{
public:
    Stacks()
    {
        File file = SPIFFS.open("/initial_stacks.txt", "r");

        while (file.available())
        {
            char next_char = file.read();
            _input_stacks += next_char;
        }

        file.close();
    }

public:
    String _input_stacks{"STACKS\n"};
};
