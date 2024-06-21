#include <gtest/gtest.h>
#include <Rucksack.h>

TEST(ExampleRucksack1, ShouldHavePriority16)
{
    Rucksack rucksack{"vJrwpWtwJgWrhcsFMMfFFhFp"};

    ASSERT_EQ(rucksack.compute_priority(), 16);
}
