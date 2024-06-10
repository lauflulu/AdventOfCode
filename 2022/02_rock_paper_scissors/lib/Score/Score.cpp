#include <Score.h>

uint32_t Score::get_total_score()
{
    return score;
}

void Score::poll(void)
{
    String message = serial.read_line();
    if (message.startsWith("A X"))
    {
        score += 4;
    }
    else if (message.startsWith("A Y"))
    {
        score += 8;
    }
    else if (message.startsWith("A Z"))
    {
        score += 3;
    }
    else if (message.startsWith("B X"))
    {
        score += 1;
    }
    else if (message.startsWith("B Y"))
    {
        score += 5;
    }
    else if (message.startsWith("B Z"))
    {
        score += 9;
    }
    else if (message.startsWith("C X"))
    {
        score += 7;
    }
    else if (message.startsWith("C Y"))
    {
        score += 2;
    }
    else if (message.startsWith("C Z"))
    {
        score += 6;
    }
}