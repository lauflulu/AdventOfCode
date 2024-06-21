#include <gtest/gtest.h>
#include <Rucksack.h>

struct TestCase
{
    String given_contents;
    uint8_t expected_priority;
};

class ExampleRucksack : public ::testing::TestWithParam<TestCase>
{
protected:
    void SetUp()
    {
    }
};

INSTANTIATE_TEST_SUITE_P(
    _, ExampleRucksack,
    testing::Values(
        TestCase{"vJrwpWtwJgWrhcsFMMfFFhFp", 16},
        TestCase{"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38},
        TestCase{"PmmdzqPrVvPwwTWBwg", 42},
        TestCase{"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22},
        TestCase{"ttgJtRGJQctTZtZT", 20},
        TestCase{"CrZsJsPPZsGzwwsLwLmpwMDw", 19}));

TEST_P(ExampleRucksack, ShouldHavePriority16)
{
    TestCase p = GetParam();
    Rucksack rucksack{p.given_contents};

    ASSERT_EQ(rucksack.compute_priority(), p.expected_priority);
}

TEST(RucksackWithWhiteSpace, ShouldHavePriority1)
{
    Rucksack rucksack{"CaaB\r\n"};

    ASSERT_EQ(rucksack.compute_priority(), 1);
}
