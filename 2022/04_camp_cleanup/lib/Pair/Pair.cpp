#include <Pair.h>

bool Pair::is_fully_contained()
{
    if (_elf_1_high <= _elf_2_high && _elf_1_low >= _elf_2_low)
    {
        return true;
    }
    if (_elf_1_high >= _elf_2_high && _elf_1_low <= _elf_2_low)
    {
        return true;
    }
    return false;
}

void Pair::_parse_input(String input)
{
    uint8_t index_of_comma = input.indexOf(",");
    String elf_1 = input.substring(0, index_of_comma);
    String elf_2 = input.substring(index_of_comma + 1);

    uint8_t index_of_minus = elf_1.indexOf("-");
    uint8_t _elf_1_low = elf_1.substring(0, index_of_minus).toInt();
    uint8_t _elf_1_high = elf_1.substring(index_of_minus + 1).toInt();

    index_of_minus = elf_2.indexOf("-");
    uint8_t _elf_2_low = elf_2.substring(0, index_of_minus).toInt();
    uint8_t _elf_2_high = elf_2.substring(index_of_minus + 1).toInt();
}
