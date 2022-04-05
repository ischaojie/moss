# -*- coding: utf-8 -*-
import calendar
import datetime
from typing import List

from moss.core.store import redis


def get_duolingo_heat(year: int):
    pass


def init_year_heat(year: int) -> List:
    for day in range(365 + calendar.isleap(year)):
        current = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day)
        yield round(current.timestamp()), 0


def get_heat(app: str, year: int) -> List:
    key = f"{app}:{year}"
    heats = redis.hgetall(key)
    if not heats:
        heats = init_year_heat(year)
        redis.hset(key, *heats)
