import solution


def test_that_load_example_data_is_a_list_of_list_of_dicts():
    data = solution.load_data("example_data.txt")
    assert isinstance(data, list)
    assert isinstance(data[0], list)
    assert isinstance(data[0][0], dict)


def test_that_load_example_data_has_the_correct_entries():
    data = solution.load_data("example_data.txt")
    assert data[0] == [{'red': 4, 'green': 0, 'blue': 3},
                       {'red': 1, 'green': 2, 'blue': 6},
                       {'red': 0, 'green': 2, 'blue': 0}]
