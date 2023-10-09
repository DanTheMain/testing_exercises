import datetime
import pytest
from typing import Callable
from faker import Faker

from functions.level_1.four_bank_parser import BankCard, SmsMessage


fake = Faker()


@pytest.fixture()
def get_random_4_digit_integer_str() -> str:
    return str(fake.pyint(1000, 9999))


@pytest.fixture()
def bank_card_last_digits(get_random_4_digit_integer_str) -> str:
    return get_random_4_digit_integer_str


@pytest.fixture()
def spent_in_name() -> str:
    return fake.company()


@pytest.fixture()
def spent_amount_str() -> float:
    return fake.pyfloat(left_digits=2, right_digits=2, positive=True)


@pytest.fixture()
def spent_datetime_str() ->str:
    return '11.11.11 11:11'


@pytest.fixture()
def test_sms(spent_amount_str, spent_datetime_str, bank_card_last_digits, spent_in_name) -> Callable:

    def inner(
            spent_amount: str | None = None,
            spent_in: str | None = None,
            spent_datetime: str | None = None,
            card_last_digits: str | None = None,
    ) -> SmsMessage:

        spent_amount = spent_amount or spent_amount_str
        spent_in = spent_in or spent_in_name
        spent_datetime = spent_datetime or spent_datetime_str
        card_last_digits = card_last_digits or bank_card_last_digits

        return SmsMessage(
                text=f'{spent_amount} $, "00000{card_last_digits} {spent_datetime} {spent_in} authcode TEST_AUTHCODE',
                author='test_author',
                sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
        )

    return inner


@pytest.fixture()
def test_bank_card(bank_card_last_digits) -> Callable:

    def inner(
            last_digits: str | None = None,
            owner_name: str | None = None,
    ) -> BankCard:

        last_digits: str = last_digits or bank_card_last_digits
        owner_name: str = owner_name or fake.name()

        return BankCard(last_digits=f"{last_digits}", owner=f"{owner_name}")

    return inner

