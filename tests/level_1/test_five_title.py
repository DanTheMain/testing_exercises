import pytest
from random import choice, choices
import string
from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    'title_base, length, increment',
    [
        ('a', 1, 0),
        ('a', 1, 1),
        (choices(string.ascii_letters, k=choice(range(2, 10))), 10, 0),
        (choice(string.ascii_letters), choice(range(2, 99)), 1),
        (choices(string.ascii_letters, k=choice(range(2, 10))), choice(range(2, 99)), 1),
    ])
def test__change_copy_item__title_length_specifications(title_base: str, length: int | None, increment: int):
    title = f"{title_base * (length + increment)}"

    assert change_copy_item(title, length) == title


def test__change_copy_item__return_default_title_with_default_max_title_length():
    default_max_title_len = 100
    default_title_over_max = f"{'a'.join(['a' * default_max_title_len])}"
    assert change_copy_item(default_title_over_max) == default_title_over_max


def test__change_copy_item__with_title_starting_with_copy_of_text_return_copy_of_title_combined():
    additional_copy_text: str = 'Copy of'
    sample_title: str = "sample"
    assert f'{additional_copy_text} {sample_title}' == change_copy_item(sample_title)


def test__change_copy_item__title_starting_with_copy_of_text_with_copy_number_return_incremented_copy_number_title():
    additional_copy_text: str = 'Copy of'
    sample_title: str = "sample"
    sample_copy_number = 0
    sample_title_with_copy_number = f'{additional_copy_text} {sample_title} ({sample_copy_number})'
    assert (
            f'{additional_copy_text} {sample_title} ({sample_copy_number + 1})' ==
            change_copy_item(sample_title_with_copy_number)
    )


def test__change_copy_item__title_starting_with_copy_of_text_and_no_copy_number():
    additional_copy_text: str = 'Copy of'
    assert f'{additional_copy_text} (2)' == change_copy_item(additional_copy_text)

