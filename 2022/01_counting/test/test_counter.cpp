#include <gtest/gtest.h>
#include <SerialCounter.h>

TEST(Counter, WhenInitializedShouldBeZero)
{
    SerialCounter counter{};
    ASSERT_EQ(counter.get_highest_count(), 0);
}