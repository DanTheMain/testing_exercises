import datetime
import pytest
import random

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date, hours, minutes, is_tomorrow',
    [
        (datetime.date.today(), 00, 00, False),
        (datetime.date.today(), 23, 59, False),
        (datetime.date.today(), random.choice(range(1, 24)), random.choice(range(10, 60)), False),
        (datetime.date.today() + datetime.timedelta(days=1), 00, 00, True),
        (datetime.date.today() + datetime.timedelta(days=1), 23, 59, True),
        (datetime.date.today() + datetime.timedelta(days=1), random.choice(range(1, 24)), random.choice(range(10, 60)),
         True),
    ]
)
def test_compose_datetime_from_today_tomorrow(date: datetime.datetime, hours: int, minutes: int, is_tomorrow: bool):
    assert compose_datetime_from(
        "tomorrow" if is_tomorrow else "today", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )

