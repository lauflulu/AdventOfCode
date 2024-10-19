#include <Pair.h>

Pair::Pair(String input)
{

    uint8_t index_of_comma = input.indexOf(",");
    String elf_1 = input.substring(0, index_of_comma);
    String elf_2 = input.substring(index_of_comma + 1);

    uint8_t index_of_minus = elf_1.indexOf("-");
    _elf_1_low = elf_1.substring(0, index_of_minus).toInt();

    _elf_1_high = elf_1.substring(index_of_minus + 1).toInt();

    index_of_minus = elf_2.indexOf("-");
    _elf_2_low = elf_2.substring(0, index_of_minus).toInt();
    _elf_2_high = elf_2.substring(index_of_minus + 1).toInt();
}

bool Pair::is_fully_contained()
{
    if (_elf_1_high == 0 and _elf_2_high == 0)
    {
        return false;
    }

    if ((_elf_1_high <= _elf_2_high) and (_elf_1_low >= _elf_2_low))
    {
        return true;
    }
    if ((_elf_1_high >= _elf_2_high) and (_elf_1_low <= _elf_2_low))
    {
        return true;
    }
    return false;
}

bool Pair::is_overlapping()
{
    if (_elf_1_high == 0 and _elf_2_high == 0)
    {
        return false;
    }

    if ((_elf_1_high >= _elf_2_low) and (_elf_1_high <= _elf_2_high))
    {
        return true;
    }
    if ((_elf_2_high >= _elf_1_low) and (_elf_2_high <= _elf_1_high))
    {
        return true;
    }
    return false;
}
