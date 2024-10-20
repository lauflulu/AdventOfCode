#include <gtest/gtest.h>
#include <fstream>
#include <string>

#include <Stacks.h>

class ExampleStacks : public ::testing::Test
{
public:
    Stacks *stacks;

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

        stacks = new Stacks(input_stacks);
    }
};

TEST_F(ExampleStacks, WhenCreatedShouldBeAtInitialState)
{
    std::cout << stacks->_input_stacks.c_str() << std::endl;
    ASSERT_EQ(1, 1);
}
