import datetime
import decimal
import pytest

from functions.level_1.four_bank_parser import BankCard, parse_ineco_expense


def test__parse_ineco_expense__card_last_digits(
    test_sms, test_bank_card, get_random_4_digit_integer_str
):
    last_digits: str = get_random_4_digit_integer_str
    test_cards: list[BankCard] = [
        test_bank_card(last_digits=last_digits),
        test_bank_card(),
        test_bank_card(last_digits=last_digits),
    ]

    assert (
        parse_ineco_expense(
            test_sms(card_last_digits=last_digits), test_cards
        ).card.last_digits
        == last_digits
    )


def test__ineco_expense__card_choice_owner_name(
    test_sms, test_bank_card, bank_card_last_digits
):
    expected_owner_name: str = "matching_card_owner_1"
    last_digits: str = bank_card_last_digits
    test_cards: list[BankCard] = [
        test_bank_card(owner_name=expected_owner_name),
        test_bank_card(),
        test_bank_card(),
    ]

    assert (
        parse_ineco_expense(
            test_sms(card_last_digits=last_digits), test_cards
        ).card.owner
        == expected_owner_name
    )


def test__ineco_expense_card__parse_amount_correctly(
    test_sms, test_bank_card, spent_amount_str, bank_card_last_digits
):
    test_amount_str = spent_amount_str

    assert parse_ineco_expense(
        test_sms(card_last_digits=bank_card_last_digits, spent_amount=spent_amount_str),
        [test_bank_card(last_digits=bank_card_last_digits)],
    ).amount == decimal.Decimal(test_amount_str)


def test__ineco_expense_card__spent_in_name(
    test_sms, test_bank_card, spent_in_name, bank_card_last_digits
):
    spent_in = spent_in_name

    assert (
        parse_ineco_expense(
            test_sms(card_last_digits=bank_card_last_digits, spent_in=spent_in),
            [test_bank_card(last_digits=bank_card_last_digits)],
        ).spent_in
        == spent_in
    )


def test__ineco_expense_card__spent_at_datetime(
    test_sms, test_bank_card, spent_datetime_str, bank_card_last_digits
):
    test_datetime = spent_datetime_str

    assert parse_ineco_expense(
        test_sms(card_last_digits=bank_card_last_digits, spent_datetime=test_datetime),
        [test_bank_card(last_digits=bank_card_last_digits)],
    ).spent_at == datetime.datetime.strptime(test_datetime, "%m.%d.%y %H:%M")


@pytest.mark.xfail(reason='failure to support cards with non-matching last digits', raises=IndexError)
def test__ineco_expense_card__error_when_last_digits_in_sms_have_no_matching_cards(
    test_sms, test_bank_card, bank_card_last_digits
):
    last_digits: str = '4321'
    non_matching_last_digits: str = last_digits[::-1]
    test_cards: list[BankCard] = [
        test_bank_card(last_digits=last_digits),
        test_bank_card(),
        test_bank_card(last_digits=last_digits),
    ]

    assert (
        parse_ineco_expense(
            test_sms(card_last_digits=non_matching_last_digits), test_cards
        ).card.last_digits
    )