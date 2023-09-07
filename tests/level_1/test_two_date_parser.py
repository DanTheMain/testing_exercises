from functions.level_1.two_date_parser import compose_datetime_from

import datetime
import random


def test_compose_datetime_from():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    test_hours, test_minutes = random.choice(range(1, 24)), random.choice(range(10, 60))
    test_time_str = f'{test_hours}:{test_minutes}'
    expected_datetime_today = datetime.datetime(today.year, today.month, today.day, test_hours, test_minutes)
    expected_datetime_tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, test_hours, test_minutes)

    assert (expected_datetime_today == compose_datetime_from("someday today", test_time_str))
    assert (expected_datetime_tomorrow == compose_datetime_from("tomorrow", test_time_str))



