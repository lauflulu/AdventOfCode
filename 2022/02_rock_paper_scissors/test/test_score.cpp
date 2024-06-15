#include <gtest/gtest.h>
#include <SerialAdapter.h>
#include <Score.h>

class TestScore : public ::testing::TestWithParam<Game>
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

INSTANTIATE_TEST_SUITE_P(
    Part1, TestScore,
    ::testing::Values(
        Game{"\r\n", 0},
        Game{"A X\r\n", 4},
        Game{"A Y\r\n", 8},
        Game{"A Z\r\n", 3},
        Game{"B X\r\n", 1},
        Game{"B Y\r\n", 5},
        Game{"B Z\r\n", 9},
        Game{"C X\r\n", 7},
        Game{"C Y\r\n", 2},
        Game{"C Z\r\n", 6},
        Game{"A Y\r\nB X\r\nC Z\r\n", 15}));

TEST_P(TestScore, WhenGivenInputShouldYieldScore)
{
    Game game = GetParam();
    mock_serial->set_input(game.outcome);

    while (mock_serial->available())
    {
        score->poll();
    }

    ASSERT_EQ(score->get_score_1(), game.score);
}
