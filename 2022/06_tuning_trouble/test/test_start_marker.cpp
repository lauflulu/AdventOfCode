#include <gtest/gtest.h>
#include <StartMarker.h>

TEST(TooShortMessage, FindStartMarkerShouldReturn0)
{
    String message = "mjq";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 0);
}

TEST(MessageWithoutStartMarker, FindStartMarkerShouldReturn0)
{
    String message = "aaaaa";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 0);
}

TEST(MessageOnlyWithStartMarker, FindStartMarkerShouldBeAtPosition4)
{
    String message = "abcdefghijklm";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 4);
}

TEST(ExampleMessage, StartMarkerShouldBeAtPosition7)
{
    String message = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 7);
}

TEST(ExampleMessage2, StartMarkerShouldBeAtPosition5)
{
    String message = "bvwbjplbgvbhsrlpgdmjqwftvncz";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 5);
}

TEST(ExampleMessage3, StartMarkerShouldBeAtPosition6)
{
    String message = "nppdvjthqldpwncqszvftbrmjlhg";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 6);
}

TEST(ExampleMessage4, StartMarkerShouldBeAtPosition10)
{
    String message = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 10);
}

TEST(ExampleMessage5, StartMarkerShouldBeAtPosition11)
{
    String message = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 11);
}

TEST(MessageWithoutStartMarker, Returns0)
{
    String message = "vqvvnggnngcgssswbblplrlflfnnnmmjppgd";

    uint32_t marker_position = find_start_marker(message);

    ASSERT_EQ(marker_position, 0);
}