#pragma once
#include <Arduino.h>

template <uint8_t n_stacks, uint8_t n_height>
class StdArrayStacks
{
public:
    StdArrayStacks(const String &input_stacks)
    {
        _parse(input_stacks);
    };

    String &to_string(String &buffer)
    {
        buffer = String("");
        for (auto i_height{0U}; i_height < stacks[0].size(); i_height++)
        {
            for (auto i_stack{0U}; i_stack < stacks.size(); i_stack++)
            {
                buffer += stacks[i_stack][i_height];
            }
            buffer += String("\n");
        }
        return buffer;
    }

public:
    std::array<std::array<char, n_height>, n_stacks> stacks;

private:
    void _parse(const String &input_stacks)
    {
        String remaining_input = String("\n") + input_stacks.substring(0, input_stacks.length() - 1);
        uint8_t i_height{0U};

        while (remaining_input.length() > 1)
        {
            int16_t end_of_line_index = remaining_input.lastIndexOf("\n");
            String current_line = remaining_input.substring(end_of_line_index + 1);
            remaining_input = remaining_input.substring(0, end_of_line_index);

            uint8_t i_stack{0U};

            for (auto i_char{0U}; i_char < current_line.length(); i_char++)
            {
                char current_character = current_line[i_char];
                if (i_char % 4 == 1)
                {
                    stacks[i_stack][i_height] = current_character;
                    i_stack++;
                }
            }
            i_height++;
        }
    };
};
