import datetime
import random

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today() + datetime.timedelta(days=1), random.choice(range(1, 24)), random.choice(range(10, 60)),
         True),
    ]
)
def test_compose_datetime_from__tomorrow(date: datetime.datetime, hours: int, minutes: int):
    assert compose_datetime_from("tomorrow", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today(), random.choice(range(1, 24)), random.choice(range(10, 60)))
    ]
)
def test_compose_datetime_from_today(date: datetime.datetime, hours: int, minutes: int, is_tomorrow: bool):
    assert compose_datetime_from("today", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today() + datetime.timedelta(days=1), 00, 00, True),
        (datetime.date.today() + datetime.timedelta(days=1), 23, 59, True),
    ]
)
def test__compose_datetime_from__tomorrow_edge_time_values(date: datetime.datetime, hours: int, minutes: int):
    assert compose_datetime_from("today", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )


@pytest.mark.parametrize(
    'date, hours, minutes',
    [
        (datetime.date.today(), 00, 00),
        (datetime.date.today(), 11, 59),
        (datetime.date.today(), 12, 00),
        (datetime.date.today(), 23, 59),
    ]
)
def test__compose_datetime_from__today_edge_time_values(date: datetime.datetime, hours: int, minutes: int):
    assert compose_datetime_from("today", f'{hours}:{minutes}'
    ) == datetime.datetime(
        date.year, date.month, date.day, hours, minutes
    )