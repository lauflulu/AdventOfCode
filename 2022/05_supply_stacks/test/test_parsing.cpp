#include <gtest/gtest.h>
#include <fstream>
#include <string>

#include <Stacks.h>

class ExampleStacks : public ::testing::Test
{
public:
    Stacks<3, 6> *stacks;

protected:
    void SetUp() override
    {
        String input_stacks{};

        std::ifstream file("data/example_stacks.txt");
        std::string line;
        while (std::getline(file, line))
        {
            input_stacks += line.c_str();
            input_stacks += "\n";
        }
        file.close();

        stacks = new Stacks<3, 6>(input_stacks);
    }
};

TEST_F(ExampleStacks, WhenCreatedShouldBeAtInitialState)
{
    ASSERT_EQ(stacks->stacks[0][0], "Z"[0]);
    ASSERT_EQ(stacks->stacks[1][0], "M"[0]);
    ASSERT_EQ(stacks->stacks[2][0], "P"[0]);

    ASSERT_EQ(stacks->stacks[0][1], "N"[0]);
    ASSERT_EQ(stacks->stacks[1][1], "C"[0]);
    ASSERT_EQ(stacks->stacks[2][1], " "[0]);

    ASSERT_EQ(stacks->stacks[0][2], " "[0]);
    ASSERT_EQ(stacks->stacks[1][2], "D"[0]);
    ASSERT_EQ(stacks->stacks[2][2], " "[0]);
}

TEST_F(ExampleStacks, WhenAtInitialStateShouldConvertToString)
{
    String expected{"ZMP\nNC \n D \n"};
    String output{""};
    stacks->to_string(output);

    ASSERT_TRUE(output.substring(0, 12) == expected);
}