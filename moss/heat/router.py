# -*- coding: utf-8 -*-

from fastapi import APIRouter

from moss.heat.model import get_duolingo_heat

router = APIRouter()


@router.get("/")
def hello():
    return {"message": "heat"}


@router.get("/duolingo/{year}")
def duolingo(year: int):
    heats = get_duolingo_heat(year)
    return heats


GOAL_KIND = ("github", "duolingo")
