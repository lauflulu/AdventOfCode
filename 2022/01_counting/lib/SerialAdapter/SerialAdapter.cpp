#include <SerialAdapter.h>

void SerialMock::set_input(String input)
{
    input_buffer = input;
}

bool SerialMock::available()
{
    return input_buffer.length() > 0;
}

String SerialMock::read_line(void)
{
    String line = input_buffer.substring(0, input_buffer.indexOf(0x0A));
    input_buffer = input_buffer.substring(input_buffer.indexOf(0x0A) + 1, input_buffer.length());
    return line;
};