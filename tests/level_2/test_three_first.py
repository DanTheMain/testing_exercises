from functions.level_2.three_first import first, NOT_SET
import random
import pytest


def test__first__return_first_item():
    assert first([1, 2, 3]) == 1


@pytest.mark.xfail(reason='error with empty list of items', raises=AttributeError)
def test__first__raise_error_without_items_and_default_param():
    assert first(items=[]) is None


def test__first__return_first_item_with_single_item_in_list():
    assert first([1]) == 1


@pytest.mark.xfail(reason='error with empty list of items and default not specified', raises=AttributeError)
def test__first__raise_error_without_items_and_not_set_default_param():
    assert first(items=[], default=NOT_SET) is None


def test__first__return_default_random_int():
    expected_default = random.choice(range(123))  # TODO: use fixture to generate random value
    assert first(items=[], default=expected_default) == expected_default


def test__first__return_none_with_default_set_to_none():
    assert first(items=[], default=None) is None


def test__first__return_default_set_to_random_string():
    random_default = random.choice(['a', 'b', 'c', 'd'])  # TODO: use random_string() fixture
    assert first(items=[], default=random_default) == random_default
