from random import randint

import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    'title_base, length, increment',
    [
        ('a', 1, 0),
        ('b', 1, 1),
        ('c', 1, 99),
    ])
def test__change_copy_item__title_length_specifications(title_base: str, length: int | None, increment: int):
    title = f"{title_base * (length + increment)}"

    assert change_copy_item(title, length) == title


def test__change_copy_item__return_default_title_with_default_max_title_length():
    default_max_title_len = 100
    default_title_over_max = f"{'a'.join(['a' * default_max_title_len])}"
    assert change_copy_item(default_title_over_max) == default_title_over_max


def test__change_copy_item__with_title_starting_with_copy_of_text_return_copy_of_title_combined():
    assert f'Copy of sample' == change_copy_item('sample')


def test__change_copy_item__copy_number_is_incremented_when_available():
    sample_copy_number = randint(0, 99)
    assert change_copy_item(f'Copy of sample ({sample_copy_number})') == f'Copy of sample ({sample_copy_number + 1})'


def test__change_copy_item__copy_number_is_added():
    assert change_copy_item('Copy of') == f'Copy of (2)'

