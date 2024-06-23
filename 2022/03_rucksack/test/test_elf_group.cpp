#include <gtest/gtest.h>
#include <ElfGroup.h>

TEST(ElfGroup1, ShouldHavePriority18)
{
    ElfGroup group_1{};

    group_1.add("vJrwpWtwJgWrhcsFMMfFFhFp");
    group_1.add("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL");
    group_1.add("PmmdzqPrVvPwwTWBwg");

    ASSERT_EQ(group_1.compute_priority(), 18);
}

TEST(ElfGroup2, ShouldHavePriority52)
{
    ElfGroup group_2{};

    group_2.add("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn");
    group_2.add("ttgJtRGJQctTZtZT");
    group_2.add("CrZsJsPPZsGzwwsLwLmpwMDw");

    ASSERT_EQ(group_2.compute_priority(), 52);
}

TEST(EmptyElfGroup, ShouldHavePriority0)
{
    ElfGroup group{};

    ASSERT_EQ(group.compute_priority(), 0);
}

TEST(IncompleteElfGroup, ShouldHavePriority0)
{
    ElfGroup group{};

    group.add("vJrwpWtwJgWrhcsFMMfFFhFp");
    group.add("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL");

    ASSERT_EQ(group.compute_priority(), 0);
}

TEST(IncompleteSecondElfGroup, ShouldHavePriority0)
{
    ElfGroup group{};

    group.add("vJrwpWtwJgWrhcsFMMfFFhFp");
    group.add("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL");
    group.add("PmmdzqPrVvPwwTWBwg");

    group.add("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn");
    group.add("ttgJtRGJQctTZtZT");

    ASSERT_EQ(group.compute_priority(), 0);
}

TEST(CompleteSecondElfGroup, ShouldHavePriority52)
{
    ElfGroup group{};

    group.add("vJrwpWtwJgWrhcsFMMfFFhFp");
    group.add("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL");
    group.add("PmmdzqPrVvPwwTWBwg");

    group.add("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn");
    group.add("ttgJtRGJQctTZtZT");
    group.add("CrZsJsPPZsGzwwsLwLmpwMDw");

    ASSERT_EQ(group.compute_priority(), 52);
}
