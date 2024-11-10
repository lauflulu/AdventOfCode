#pragma once
#include <Arduino.h>

uint32_t find_packet_marker(const String &message);
uint32_t find_message_marker(const String &message);

uint32_t _find_marker(const String &message, const uint8_t MARKER_SIZE);
void _shift(char c, char buffer[], uint8_t size);
