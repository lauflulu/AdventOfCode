#include <gtest/gtest.h>
#include <SerialAdapter.h>
#include <Score.h>

class TestScore : public ::testing::Test
{
protected:
    SerialMock *mock_serial;
    Score *score;
    virtual void SetUp()
    {
        mock_serial = new SerialMock();
        score = new Score(*mock_serial);
    }
};

TEST_F(TestScore, WhenInitializedIsZero)
{
    ASSERT_EQ(score->get_total_score(), 0);
}

TEST_F(TestScore, WhenAXShouldBe4)
{
    mock_serial->set_input("A X\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 4);
}

TEST_F(TestScore, WhenAYShouldBe8)
{
    mock_serial->set_input("A Y\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 8);
}

TEST_F(TestScore, WhenAZShouldBe3)
{
    mock_serial->set_input("A Z\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 3);
}

TEST_F(TestScore, WhenBXShouldBe1)
{
    mock_serial->set_input("B X\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 1);
}

TEST_F(TestScore, WhenBYShouldBe5)
{
    mock_serial->set_input("B Y\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 5);
}

TEST_F(TestScore, WhenBZShouldBe9)
{
    mock_serial->set_input("B Z\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 9);
}

TEST_F(TestScore, WhenCXShouldBe7)
{
    mock_serial->set_input("C X\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 7);
}

TEST_F(TestScore, WhenCYShouldBe2)
{
    mock_serial->set_input("C Y\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 2);
}

TEST_F(TestScore, WhenCZShouldBe6)
{
    mock_serial->set_input("C Z\r\n");

    score->poll();

    ASSERT_EQ(score->get_total_score(), 6);
}