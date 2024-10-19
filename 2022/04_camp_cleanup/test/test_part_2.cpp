#include <gtest/gtest.h>
#include <Pair.h>

TEST(ExamplePair1, IsNotOverlapping)
{
    Pair pair{String("2-4,6-8")};
    ASSERT_FALSE(pair.is_overlapping());
}

TEST(ExamplePair2, IsNotOverlapping)
{
    Pair pair{String("2-3,4-5")};
    ASSERT_FALSE(pair.is_overlapping());
}

TEST(ExamplePair3, IsNotOverlapping)
{
    Pair pair{String("5-7,7-9")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(ExamplePair4, IsNotOverlapping)
{
    Pair pair{String("2-8,3-7")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(ExamplePair5, IsNotOverlapping)
{
    Pair pair{String("6-6,4-6")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(ExamplePair6, IsNotOverlapping)
{
    Pair pair{String("2-6,4-8")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(InputPair1, IsNotOverlapping)
{
    Pair pair{String("24-66,23-25\r\n")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(InputPair2, IsNotOverlapping)
{
    Pair pair{String("3-3,2-80\r\n")};
    ASSERT_TRUE(pair.is_overlapping());
}

TEST(EmptyInput, IsOverlappingWhenReceivingFirstSerialMessageShouldBeFalse)
{
    Pair pair{String("\r\n")};
    ASSERT_FALSE(pair.is_overlapping());
}
