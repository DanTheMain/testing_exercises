import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_ineco_expense_return_type():
    assert isinstance(parse_ineco_expense(SmsMessage(
        text='12.34 $, "000001234 11.11.11 11:11 test_shop authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    ), [BankCard(last_digits='1234', owner='matching_card_owner_1')]), Expense)


def test_ineco_expense_card_choice():
    expected_last_digits, expected_owner_name = '1234', 'matching_card_owner_1'
    test_cards = [BankCard(last_digits=f'{expected_last_digits}', owner=f'{expected_owner_name}'),
                  BankCard(last_digits='5432', owner='non_matching_card_owner_1'),
                  BankCard(last_digits=f'{expected_last_digits}', owner='non_matching_card_owner_2')]
    test_sms = SmsMessage(
        text='12.34 $, "000001234 11.11.11 11:11 test_shop authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    )

    actual_test_card = parse_ineco_expense(test_sms, test_cards).card
    assert(actual_test_card.last_digits == expected_last_digits and actual_test_card.owner == expected_owner_name)


def test_ineco_expense_amount():
    test_amount_str = "12.34"
    expected_test_amount = decimal.Decimal(f"{test_amount_str}")

    assert (parse_ineco_expense(SmsMessage(
        text=f'{test_amount_str} $, "000001234 11.11.11 11:11 test_shop authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    ), [BankCard(last_digits='1234', owner='matching_card_owner_1')]).amount == expected_test_amount)


def test_ineco_expense_spent_in_name():
    spent_in_str = 'test_shop'

    assert (parse_ineco_expense(SmsMessage(
        text=f'12.34 $, "000001234 11.11.11 11:11 {spent_in_str} authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    ), [BankCard(last_digits='1234', owner='matching_card_owner_1')]).spent_in == spent_in_str)


def test_ineco_expense_spent_at_datetime():
    test_dt_str = '11.11.11 11:11'
    expected_dt = datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S')

    assert (parse_ineco_expense(SmsMessage(
        text=f'12.34 $, "000001234 {test_dt_str} test_shop authcode TEST_AUTHCODE',
        author='test_author',
        sent_at=datetime.datetime.strptime('11/11/11 11:11:00', '%m/%d/%y %H:%M:%S'),
    ), [BankCard(last_digits='1234', owner='matching_card_owner_1')]).spent_at == expected_dt)

