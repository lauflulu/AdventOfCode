#pragma once
#include <Arduino.h>

uint32_t find_start_marker(const String &message);
void shift(char c, char *buffer, uint8_t size);
