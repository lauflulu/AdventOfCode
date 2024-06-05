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
    mock_serial->set_input(String("54\r\n"));

    counter->poll();

    ASSERT_EQ(counter->get_highest_count(), 54);
}

TEST_F(TestCounter, WhenPollsIntegerSequenceShouldAddToHighestCount)
{
    mock_serial->set_input(String("42\r\n0\r\n314\r\n"));

    for (auto i{0U}; i < 3U; i++)
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 356);
}

TEST_F(TestCounter, WhenPollsTwoIntegerSequencesShouldKeepHighestCount)
{
    mock_serial->set_input(String("314\r\n\r\n42\r\n"));

    for (auto i{0U}; i < 3U; i++)
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 314);
}