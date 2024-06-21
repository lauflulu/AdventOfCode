#include <gtest/gtest.h>
#include <Rucksack.h>

TEST(ExampleRucksack1, ShouldHavePriority16)
{
    Rucksack rucksack{"vJrwpWtwJgWrhcsFMMfFFhFp"};

    ASSERT_EQ(rucksack.compute_priority(), 16);
}

TEST(RucksackWithWhiteSpace, ShouldHavePriority1)
{
    Rucksack rucksack{"CaaB\r\n"};

    ASSERT_EQ(rucksack.compute_priority(), 1);
}
