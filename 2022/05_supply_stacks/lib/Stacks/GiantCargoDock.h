#pragma once
#include <Arduino.h>

struct Box
{
    char cargo;
    Box *below;
};

class Stack
{
public:
    Stack() : _top(nullptr) {};
    ~Stack()
    {
        while (_top)
        {
            pop();
        }
    };

    bool empty()
    {
        return !_top;
    }

    void push(char cargo)
    {
        Box *box = new Box;
        box->below = _top;
        box->cargo = cargo;
        _top = box;
    }

    char pop()
    {
        if (empty())
        {
            return 0x00;
        }
        Box *remove = _top;
        _top = remove->below;
        char value = remove->cargo;
        delete remove;
        return value;
    }

    char get()
    {
        if (empty())
        {
            return 0x00;
        }
        return _top->cargo;
    }

private:
    Box *_top;
};

class GiantCargoDock
{
public:
    GiantCargoDock() {};

    GiantCargoDock(const String &input_stacks)
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

    void push_row(const String &line)
    {
        uint8_t i_stack{0U};

        for (auto i_char{0U}; i_char < line.length(); i_char++)
        {
            if (i_char % 4 == 1)
            {
                char current_character = line.charAt(i_char);
                if (0x41 <= current_character & current_character <= 0x5A)
                {
                    stacks[i_stack].push(current_character);
                }
                i_stack++;
            }
        }
    }

    void read_top(String &buffer)
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

    void process_instruction(const String &instruction)
    {
    }

public:
    std::array<Stack, 3> stacks{};

private:
    void _parse(const String &input_stacks) {

    };
};
