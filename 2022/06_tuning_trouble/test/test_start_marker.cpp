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

TEST(MessageOnlyWithStartMarker, FindStartMarkerShouldReturn0)
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