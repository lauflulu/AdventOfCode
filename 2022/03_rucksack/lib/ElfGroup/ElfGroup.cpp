#include "ElfGroup.h"

void ElfGroup::add(String contents)
{
    contents.trim();

    uint8_t i_current{0U};
    for (auto i{0U}; i < 3; i++)
    {
        if (_contents[i] == "")
        {
            break;
        }
        i_current++;
    }

    if (i_current == 3)
    {
        for (auto i{0U}; i < 3; i++)
        {
            _contents[i] = "";
        }
        _contents[0] = contents;
    }
    else
    {
        _contents[i_current] = contents;
    }
}

uint8_t ElfGroup::compute_priority()
{
    char badge = find_common_item();
    char a = String("a").charAt(0);
    char z = String("z").charAt(0);
    char A = String("A").charAt(0);
    char Z = String("Z").charAt(0);

    if (a <= badge & badge <= z)
    {
        return badge - a + 1;
    }
    if (A <= badge & badge <= Z)
    {
        return badge - A + 27;
    }
    return 0;
}

char ElfGroup::find_common_item()
{
    for (char item_1 : _contents[0])
    {
        for (char item_2 : _contents[1])
        {
            for (char item_3 : _contents[2])
            {
                if (item_1 == item_2 & item_1 == item_3)
                {
                    return item_1;
                }
            }
        }
    }
    return 0;
}
