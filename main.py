from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from models import Base
from models.weather import WeatherModel
from sqlalchemy.ext.asyncio import AsyncSession
from db_connection import get_session, engine
from api_receiver import get_data
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.get("/main", response_class=HTMLResponse)
async def weather_page(request: Request):
    return templates.TemplateResponse(
        "main.html", {"request": request, "weather": None}
    )


@app.post("/main", response_class=HTMLResponse)
async def weather_post(
    session: SessionDep,
    request: Request,
    city: str = Form(...),
):

    city = city.strip()
    if not city or city.isdigit():
        return templates.TemplateResponse(
            "main.html",
            {
                "request": request,
                "error": f"Incorrect city name. Please try again!",
            },
        )

    res = await get_data(city)

    if not res or "main" not in res or "wind" not in res:
        return templates.TemplateResponse(
            "main.html",
            {
                "request": request,
                "error": f"City '{city}' not found. Please try again!",
            },
        )

    new_weather = WeatherModel(
        city=city,
        temp=round(res["main"]["temp"] - 273, 2),
        temp_max=round(res["main"]["temp_max"] - 273, 2),
        temp_min=round(res["main"]["temp_min"] - 273, 2),
        feels_like=round(res["main"]["feels_like"] - 273, 2),
        wind_speed=res["wind"]["speed"],
        query_timestamp=datetime.now(),
    )

    session.add(new_weather)

    await session.commit()

    result = await session.execute(
        select(WeatherModel).order_by(WeatherModel.query_timestamp.desc()).limit(10)
    )
    history = result.scalars().all()

    return templates.TemplateResponse(
        "main.html",
        {"request": request, "weather": new_weather, "history": history},
    )
