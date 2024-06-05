#include <Counter.h>

uint32_t Counter::get_highest_count()
{
    return highest_count;
}

void Counter::poll(void)
{
    String current_line = serial.read_line();

    current_count += current_line.toInt();

    if (current_count > highest_count)
    {
        highest_count = current_count;
    }
}