#include <gtest/gtest.h>
#include <Pair.h>

TEST(ExamplePair1, IsNotFullyContained)
{
    Pair pair{String("2-4,6-8")};
    ASSERT_EQ(false, pair.is_fully_contained());
}

TEST(ExamplePair2, IsNotFullyContained)
{
    Pair pair{String("2-3,4-5")};
    ASSERT_EQ(false, pair.is_fully_contained());
}

TEST(ExamplePair3, IsNotFullyContained)
{
    Pair pair{String("5-7,7-9")};
    ASSERT_EQ(false, pair.is_fully_contained());
}

TEST(ExamplePair4, IsFullyContained)
{
    Pair pair{String("2-8,3-7")};
    ASSERT_EQ(true, pair.is_fully_contained());
}

TEST(ExamplePair5, IsFullyContained)
{
    Pair pair{String("6-6,4-6")};
    ASSERT_EQ(true, pair.is_fully_contained());
}

TEST(ExamplePair6, IsNotFullyContained)
{
    Pair pair{String("2-6,4-8")};
    ASSERT_EQ(false, pair.is_fully_contained());
}

TEST(InputPair1, IsNotFullyContained)
{
    Pair pair{String("24-66,23-25\r\n")};
    ASSERT_EQ(false, pair.is_fully_contained());
}

TEST(InputPair2, IsFullyContained)
{
    Pair pair{String("3-3,2-80\r\n")};
    ASSERT_EQ(true, pair.is_fully_contained());
}
