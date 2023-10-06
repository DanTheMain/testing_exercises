from random import choice, randint

import pytest
from faker import Faker

fake = Faker()


@pytest.fixture()
def make_repeatable_str():
    def gen_str_fn(base_str: str, count: int, sep: str) -> str:
        return sep.join(count * (base_str,))
    return gen_str_fn


@pytest.fixture()
def random_int_from_range():
    def inner(upper_range: int) -> int:
        return randint(1, upper_range)
    return inner


@pytest.fixture()
def gen_random_string():
    return choice(fake.text().split())

