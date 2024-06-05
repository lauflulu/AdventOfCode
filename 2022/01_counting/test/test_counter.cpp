#include <gtest/gtest.h>
#include <SerialAdapter.h>
#include <Counter.h>

class TestCounter : public ::testing::Test
{
protected:
    SerialMock *mock_serial;
    Counter *counter;
    virtual void SetUp()
    {
        mock_serial = new SerialMock();
        counter = new Counter(*mock_serial);
    }
};

TEST_F(TestCounter, WhenInitializedShouldBeZero)
{

    ASSERT_EQ(counter->get_highest_count(), 0);
}

TEST_F(TestCounter, WhenPollsIntegerShouldAddToHighestCount)
{
    mock_serial->set_input(String("54\n\r"));

    counter->poll();

    ASSERT_EQ(counter->get_highest_count(), 54);
}