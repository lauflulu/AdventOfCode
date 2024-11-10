#include <StartMarker.h>

uint32_t find_packet_marker(const String &message)
{
    const uint8_t MARKER_SIZE{4U};
    return _find_marker(message, MARKER_SIZE);
}

uint32_t find_message_marker(const String &message)
{
    const uint8_t MARKER_SIZE{14U};
    return _find_marker(message, MARKER_SIZE);
}

uint32_t _find_marker(const String &message, const uint8_t MARKER_SIZE)
{
    const uint32_t LENGTH = message.length();
    if (LENGTH < MARKER_SIZE)
    {
        return 0;
    }

    char buffer[15]{0x40};
    buffer[MARKER_SIZE] = 0;
    uint8_t block_timer{MARKER_SIZE - 1};
    for (auto i_message{0}; i_message < LENGTH; i_message++)
    {
        char next = message.charAt(i_message);

        for (auto i_marker{0}; i_marker < MARKER_SIZE - 1; i_marker++)
        {
            if (buffer[i_marker] == next)
            {
                block_timer = (i_marker + 1 > block_timer) ? i_marker + 1 : block_timer;
            }
        }
        if (block_timer == 0)
        {
            return i_message + 1;
        }
        block_timer--;

        _shift(next, buffer, MARKER_SIZE - 1);
    }

    return 0;
}

void _shift(char c, char buffer[], uint8_t size)
{
    for (auto i{0}; i < size - 1; i++)
    {
        buffer[i] = buffer[i + 1];
    }
    buffer[size - 1] = c;
}