#include <StartMarker.h>

uint32_t find_start_marker(const String &message)
{
    const uint32_t LENGTH = message.length();
    const uint8_t MARKER_SIZE{4U};
    if (LENGTH < MARKER_SIZE)
    {
        return 0;
    }

    char buffer[MARKER_SIZE]{0};
    uint8_t block_timer{MARKER_SIZE - 1};
    for (auto i_message{0}; i_message < LENGTH; i_message++)
    {
        char next = message.charAt(i_message);
        uint8_t current_buffer_position = i_message % MARKER_SIZE;
        buffer[current_buffer_position] = next;

        for (auto i_marker{1U}; i_marker < MARKER_SIZE; i_marker++)
        {
            uint8_t i = (i_marker + current_buffer_position) % MARKER_SIZE;
            if (buffer[i] == next)
            {
                block_timer = i_marker;
                break;
            }
            if ((i_marker == MARKER_SIZE - 1) && (block_timer == 0))
            {
                return i_message + 1;
            }
        }
        block_timer = block_timer == 0 ? 0 : block_timer - 1;
    }

    return 0;
}