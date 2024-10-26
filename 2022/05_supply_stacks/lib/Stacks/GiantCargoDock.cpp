#include <GiantCargoDock.h>

GiantCargoDock::GiantCargoDock(const String &input_stacks)
{
    String remaining_input = String("\n") + input_stacks.substring(0, input_stacks.length() - 1);
    uint8_t i_height{0U};

    while (remaining_input.length() > 1)
    {
        int16_t end_of_line_index = remaining_input.lastIndexOf("\n");
        String current_line = remaining_input.substring(end_of_line_index + 1);
        remaining_input = remaining_input.substring(0, end_of_line_index);

        push_row(current_line);
    }
};

void GiantCargoDock::push_row(const String &line)
{
    uint8_t i_stack{0U};

    for (auto i_char{0U}; i_char < line.length(); i_char++)
    {
        if (i_char % 4 == 1)
        {
            char current_character = line.charAt(i_char);
            const char A{0x41}, Z{0x5A};
            if (A <= current_character & current_character <= Z)
            {
                stacks[i_stack].push(current_character);
            }
            i_stack++;
        }
    }
}

void GiantCargoDock::read_top(String &buffer)
{
    buffer = String("");
    for (auto &stack : stacks)
    {
        char cargo = stack.get();
        if (cargo)
        {
            buffer += cargo;
        }
    }
}

// void GiantCargoDock::process_instruction(const String &instruction)
// {
// }