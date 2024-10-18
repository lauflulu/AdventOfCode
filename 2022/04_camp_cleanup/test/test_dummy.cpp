#include <gtest/gtest.h>
#include <Pair.h>

TEST(ExamplePair1, IsNotFullyContained)
{
    Pair pair{String("2-4,6-8")};
    ASSERT_EQ(false, pair.is_fully_contained());
}
