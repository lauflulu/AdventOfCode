#include <gtest/gtest.h>
#include <StartMarker.h>

TEST(ExampleMessage, StartMarkerShouldBeAtPosition19)
{
    String message = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";

    uint32_t marker_position = find_message_marker(message);

    ASSERT_EQ(marker_position, 19);
}

TEST(ExampleMessage, StartMarkerShouldBeAtPosition23)
{
    String message = "bvwbjplbgvbhsrlpgdmjqwftvncz";

    uint32_t marker_position = find_message_marker(message);

    ASSERT_EQ(marker_position, 23);
}
