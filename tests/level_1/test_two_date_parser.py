import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today(), 00, 00),
        (datetime.date.today(), 12, 00),
        (datetime.date.today(), 23, 59),
    ]
)
def test_compose_datetime_from_today(date: datetime.datetime, hours: int, minutes: int):
    assert compose_datetime_from("today", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today() + datetime.timedelta(days=1), 12, 00),
        (datetime.date.today() + datetime.timedelta(days=1), 00, 00),
        (datetime.date.today() + datetime.timedelta(days=1), 23, 59),
    ]
)
def test_compose_datetime_from_tomorrow(date: datetime.datetime, hours: int, minutes: int):
    assert compose_datetime_from("tomorrow", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )
