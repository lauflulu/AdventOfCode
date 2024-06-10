#include <Score.h>

uint32_t Score::get_total_score()
{
    return 0;
}

void Score::poll(void)
{
    String message = serial.read_line();
}