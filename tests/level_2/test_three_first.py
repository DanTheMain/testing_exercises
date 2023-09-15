from functions.level_2.three_first import first, NOT_SET
import random
from pytest import raises


def test__first__with_first_item():
    assert first([1,2,3]) == 1


def test__first_with_no_items_with_default_default():
    with raises(AttributeError):
        first(items=[])


def test__first_with_single_item():
    assert first([1]) == 1


def test__first_with_default_as_not_set():
    with raises(AttributeError):
        first(items=[], default=NOT_SET)


def test__first_with_default_set_to_random_int():
    expected_default = random.choice(range(123))
    assert first(items=[], default=expected_default) == expected_default


def test__first_with_default_set_to_none():
    assert first(items=[], default=None) is None


def test__first_with_default_set_to_a_string():
    random_default = random.choice(['q', 'w', 'er', 'TY'])
    assert first(items=[], default=random_default) == random_default

