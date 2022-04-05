# -*- coding: utf-8 -*-
from datetime import date

from moss.heat.model import init_year_heat


def test_init_year_heat():
    year_heat = init_year_heat(2022)
    for year, total in year_heat:
        current = date.fromtimestamp(year)
        assert current.year == 2022
        assert total == 0
