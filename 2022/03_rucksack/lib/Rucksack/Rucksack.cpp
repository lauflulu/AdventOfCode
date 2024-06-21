#include "Rucksack.h"

Rucksack::Rucksack(String contents)
{
    _contents = contents;
}

uint8_t Rucksack::compute_priority()
{
    split_compartments();
    char duplicate_item = find_duplicate();
    const char *a = "a";
    return duplicate_item - a[0] + 1;
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
