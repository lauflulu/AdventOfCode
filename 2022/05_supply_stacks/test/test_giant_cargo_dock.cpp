#include <gtest/gtest.h>
#include <fstream>
#include <string>

#include <GiantCargoDock.h>

TEST(SingleStack, WhenInitializedShouldBeEmpty)
{
    Stack single_stack{};
    ASSERT_TRUE(single_stack.empty());
}

TEST(SingleStack, GivenCharIsPushedWhenGetShouldNotBeEmpty)
{
    Stack single_stack{};
    single_stack.push(0x34);
    ASSERT_FALSE(single_stack.empty());
}

TEST(SingleStack, GivenCharIsPushedWhenGetShouldReturnChar)
{
    Stack single_stack{};
    single_stack.push(0x12);
    ASSERT_EQ(0x12, single_stack.get());
}

TEST(CargoDock, WhenInitializedShouldReadNothing)
{
    GiantCargoDock dock{};
    String expected{""};
    String output{""};

    dock.read_top(output);
    ASSERT_TRUE(output == expected);
}

TEST(CargoDock, WhenOneRowPushedShouldBeOnTop)
{
    GiantCargoDock dock{};
    String expected{"AAA"};
    String output{""};

    dock.push_row(String("[A] [A] [A]"));

    dock.read_top(output);
    ASSERT_TRUE(output == expected);
}

TEST(CargoDock, WhenIncompleteRowPushedShouldBeOnTop)
{
    GiantCargoDock dock{};
    String expected{"ABC"};
    String output{""};

    dock.push_row(String("[A] [A] [A]"));
    dock.push_row(String("    [B] [B]"));
    dock.push_row(String("        [C]"));

    dock.read_top(output);
    ASSERT_TRUE(output == expected);
}

class ExampleDock : public ::testing::Test
{
public:
    GiantCargoDock *stacks;

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

        stacks = new GiantCargoDock{input_stacks};
    }
};

TEST_F(ExampleDock, WhenAtInitialStateShouldReadNDP)
{
    String expected{"NDP"};
    String output{""};
    stacks->read_top(output);

    ASSERT_STREQ(output.c_str(), expected.c_str());
}

TEST_F(ExampleDock, WhenFirstIntstructionShouldReadDCP)
{
    String expected{"DCP"};
    String output{""};

    stacks->process(String("move 1 fom 2 to 1\n"));

    stacks->read_top(output);
    ASSERT_STREQ(output.c_str(), expected.c_str());
}