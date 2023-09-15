from functions.level_2.one_median import get_median_value
import pytest


def test__get_median_value__with_no_items():
    assert get_median_value([]) is None


@pytest.mark.xfail(reason='failed on attempt to access second element', raises=IndexError)
def test__get_median_value__raises_error_with_single_item():
    assert get_median_value([1]) == 1


@pytest.mark.xfail(reason='failed on attempt to work with list argument being too short', raises=IndexError)
def test__get_median_value__raises_error_with_four_items():
    assert get_median_value([1, 1, 2, 3]) == 1


def test__get_median_value__spec_median():
    expected_median = 5
    items: list[int] = [11, 9, 3, expected_median, expected_median]

    assert get_median_value(items) == expected_median


def test__get_median_value__should_work_with_even_value_count_in_list():
    assert get_median_value([11, 9, 3, 1, 0, 23]) == 11


def test__get_median_value__should_work_with_odd_value_count_in_list():
    assert get_median_value([11, 9, 3, 1, 23, 111, 111]) == 23


def test__get_median_value__multiple_matching_values():
    assert get_median_value([22 for _ in range(22)]) == 22


def test__get_median_value__mixed_positive_negative_values():
    assert get_median_value([-11, 9, -3, 1, -23, -111, 111]) == -23
