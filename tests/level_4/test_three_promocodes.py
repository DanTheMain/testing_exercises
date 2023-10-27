from unittest.mock import patch

import pytest

from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize("promocode_len", [len for len in range(10)])
def test__generate_promocode__returns_words_of_specified_len(promocode_len):
    assert len(generate_promocode(promocode_len)) == promocode_len


def test__generate_promocode__returns_default_len_promocode():
    assert len(generate_promocode()) == 8


def test__generate_promocode__uses_random_choices_to_generate_response(
    generate_test_promocode, promocode_test_char, promocode_test_len
):
    with patch(
        "functions.level_4.three_promocodes.random.choice"
    ) as random_choice_mock:
        random_choice_mock.return_value = promocode_test_char
        assert generate_promocode(promocode_test_len) == generate_test_promocode
