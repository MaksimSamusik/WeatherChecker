from datetime import datetime
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class WeatherModel(Base):
    __tablename__ = "weather"

    city: Mapped[str] = mapped_column(String, nullable=False)
    temp: Mapped[float] = mapped_column(Float, nullable=False)
    temp_max: Mapped[float] = mapped_column(Float, nullable=False)
    temp_min: Mapped[float] = mapped_column(Float, nullable=False)
    feels_like: Mapped[float] = mapped_column(Float, nullable=False)
    wind_speed: Mapped[float] = mapped_column(Float, nullable=False)
    query_timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)