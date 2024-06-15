#include <Score.h>

uint32_t Score::get_total_score()
{
    return score;
}

void Score::poll(void)
{
    String message = serial.read_line();
    for (uint8_t i{0U}; i < 9; i++)
    {
        if (message.startsWith(score_map_1[i].outcome))
        {
            score += score_map_1[i].score;
        }
    }
}