from random import choice
from pytest import fixture


@fixture()
def gen_str():
    def gen_str_fn(base_str: str, count: int, sep: str) -> str:
        return sep.join(count * (base_str,))
    return gen_str_fn


@fixture()
def random_int_from_range():
    def inner(upper_range: int) -> int:
        return choice(range(upper_range))
    return inner


@fixture()
def random_string():
    return choice(['a', 'b', 'c', 'd'])  #TODO - improve on choices and char numbers

