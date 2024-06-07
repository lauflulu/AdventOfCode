#include <Counter.h>

uint32_t Counter::get_highest_count()
{
    return top3_counts[2];
}

uint32_t Counter::get_top3_count()
{
    uint32_t sum{0U};
    for (auto i{0U}; i < 3U; i++)
    {
        sum += top3_counts[i];
    }
    return sum;
}

void Counter::poll(void)
{
    String message = serial.read_line();
    bool count_complete = message.charAt(0) == 0x0D;

    if (!count_complete)
    {
        current_count += message.toInt();
    }
    else
    {
        update_top3();
        current_count = 0;
    }
}

void Counter::update_top3()
{
    if (current_count >= top3_counts[0])
    {
        // overwrite lowest count
        top3_counts[0] = current_count;
        // bubble sort ascending
        for (auto i{0U}; i < 2U; i++)
        {
            if (top3_counts[i + 1] < top3_counts[i])
            {
                uint32_t smaller = top3_counts[i + 1];
                uint32_t larger = top3_counts[i];
                top3_counts[i] = smaller;
                top3_counts[i + 1] = larger;
            }
        }
    }
}