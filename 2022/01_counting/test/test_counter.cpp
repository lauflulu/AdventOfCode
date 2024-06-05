#include <gtest/gtest.h>
#include <Counter.h>

class TestCounter : public ::testing::Test
{
protected:
    Counter *counter;
    virtual void SetUp()
    {
        SerialMock mock_serial;
        counter = new Counter(mock_serial);
    }
};

TEST_F(TestCounter, WhenInitializedShouldBeZero)
{

    ASSERT_EQ(counter->get_highest_count(), 0);
}