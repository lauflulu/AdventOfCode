#include "Rucksack.h"

Rucksack::Rucksack(String contents)
{
    _contents = contents;
    _contents.trim();
}

uint8_t Rucksack::compute_priority()
{
    split_compartments();
    char duplicate_item = find_duplicate();
    char a = String("a").charAt(0);
    char z = String("z").charAt(0);
    char A = String("A").charAt(0);
    char Z = String("Z").charAt(0);

    if (a <= duplicate_item & duplicate_item <= z)
    {
        return duplicate_item - a + 1;
    }
    if (A <= duplicate_item & duplicate_item <= Z)
    {
        return duplicate_item - A + 27;
    }
    return 0;
}

void Rucksack::split_compartments()
{
    uint8_t number_of_items = _contents.length();
    _left_compartment = _contents.substring(0, number_of_items / 2);
    _right_compartment = _contents.substring(number_of_items / 2);
}

char Rucksack::find_duplicate()
{
    for (char left_item : _left_compartment)
    {
        for (char right_item : _right_compartment)
        {
            if (left_item == right_item)
            {
                return left_item;
            }
        }
    }
    return 0;
}
