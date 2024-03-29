# -*- coding: utf-8 -*-

import uvicorn
from fastapi import FastAPI

from moss.heat.router import router as heat_router

app = FastAPI()

app.include_router(heat_router, prefix="/heat", tags=["heat"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
