#include <Counter.h>

uint32_t Counter::get_highest_count()
{
    return highest_count;
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
    String current_line = serial.read_line();

    if (current_line.charAt(0) == 0x0D)
    {
        if (current_count > highest_count)
        {
            highest_count = current_count;
        }

        if (current_count < top3_counts[0])
        {
        }
        else
        {
            top3_counts[0] = current_count; // overwrite lowest count
            // bubble sort
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

        current_count = 0;
    }
    else
    {
        current_count += current_line.toInt();
    }
}