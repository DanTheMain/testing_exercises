import datetime
import decimal
from typing import NamedTuple
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    test_cards = [BankCard(last_digits='1234', owner='matching_card_owner_1'),
                  BankCard(last_digits='5432', owner='non_matching_card_owner_1'),
                  BankCard(last_digits='1234', owner='matching_card_owner_2')]
    test_sms = SmsMessage(
        text='12.34 $, "000001234 11.11.11 11:11 test_shop authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    )

    expected_expense = Expense(
        amount=decimal.Decimal('12.34'),
        card=test_cards[0],
        spent_in='test_shop',
        spent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'))
    assert(expected_expense
           ==
           parse_ineco_expense(test_sms, test_cards))




