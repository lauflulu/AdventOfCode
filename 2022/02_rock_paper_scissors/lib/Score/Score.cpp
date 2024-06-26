#include <Score.h>

uint32_t Score::get_score_1()
{
    return score_1;
}

uint32_t Score::get_score_2()
{
    return score_2;
}

void Score::poll(void)
{
    String message = serial.read_line();
    update_score_1(message);
    update_score_2(message);
}

void Score::update_score_1(String &message)
{
    for (uint8_t i{0U}; i < 9; i++)
    {
        if (message.startsWith(score_map_1[i].outcome))
        {
            score_1 += score_map_1[i].score;
        }
    }
}

void Score::update_score_2(String &message)
{
    for (uint8_t i{0U}; i < 9; i++)
    {
        if (message.startsWith(score_map_2[i].outcome))
        {
            score_2 += score_map_2[i].score;
        }
    }
}
