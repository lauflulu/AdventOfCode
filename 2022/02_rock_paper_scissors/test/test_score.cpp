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
