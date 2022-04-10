# -*- coding: utf-8 -*-

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from moss.heat.model import get_heat

router = APIRouter()

HEAT_KIND = ("github", "duolingo")


@router.get("/{app}/{year}")
def heat(app, year):
    if app not in HEAT_KIND:
        raise HTTPException(status_code=400, detail="Invalid app kind")
    return get_heat(app, year)
