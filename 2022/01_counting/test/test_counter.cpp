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
    mock_serial->set_input(String("54\r\n\r\n"));

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 54);
}

TEST_F(TestCounter, WhenPollsIntegerSequenceShouldAddToHighestCount)
{
    mock_serial->set_input(String("42\r\n0\r\n314\r\n\r\n"));

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 356);
}

TEST_F(TestCounter, WhenPollsTwoIntegerSequencesShouldKeepHighestCount)
{
    mock_serial->set_input(String("314\r\n\r\n42\r\n\r\n"));

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 314);
}

TEST_F(TestCounter, WhenPolls32BitIntegerShouldHaveCorrectHighestCount)
{
    mock_serial->set_input(String("3141592\r\n\r\n"));

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 3141592);
}

TEST_F(TestCounter, WhenGivenExampleInputShouldComputeHighestCount)
{
    String example_input =
        "1000\r\n"
        "2000\r\n"
        "3000\r\n "
        "\r\n"
        "4000\r\n"
        "\r\n"
        "5000\r\n"
        "6000\r\n"
        "\r\n"
        "7000\r\n"
        "8000\r\n"
        "9000\r\n"
        "\r\n"
        "10000\r\n"
        "\r\n";
    mock_serial->set_input(example_input);

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_highest_count(), 24000);
}

TEST_F(TestCounter, WhenGivenExampleInputShouldComputeTop3Count)
{
    String example_input =
        "1000\r\n"
        "2000\r\n"
        "3000\r\n "
        "\r\n"
        "4000\r\n"
        "\r\n"
        "5000\r\n"
        "6000\r\n"
        "\r\n"
        "7000\r\n"
        "8000\r\n"
        "9000\r\n"
        "\r\n"
        "10000\r\n"
        "\r\n";
    mock_serial->set_input(example_input);

    while (mock_serial->available())
    {
        counter->poll();
    }

    ASSERT_EQ(counter->get_top3_count(), 45000);
}