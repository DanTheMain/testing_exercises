import pytest

from functions.level_2.three_first import first, NOT_SET


def test__first__return_first_item():
    assert first([1, 2, 3]) == 1


def test__first__raise_error_when_items_empty_and_default_not_set():
    with pytest.raises(AttributeError):
        first(items=[])


def test__first__return_first_item_with_single_item_in_list():
    assert first([1]) == 1


def test__first__raise_error_when_default_as_not_set():
    with pytest.raises(AttributeError):
        first(items=[], default=NOT_SET)


def test__first__return_default_int_value_when_items_empty(random_int_from_range):
    r_int = random_int_from_range(123)
    assert first(items=[], default=r_int) == r_int


def test__first__return_none_with_default_set_to_none():
    assert first(items=[], default=None) is None


def test__first__return_default_set_to_string(gen_random_string):
    assert first(items=[], default=gen_random_string) == gen_random_string
