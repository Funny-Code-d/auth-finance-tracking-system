import datetime
from sqlalchemy.schema import Sequence
from sqlalchemy import CheckConstraint, ForeignKey, Column
from sqlalchemy import String, Integer, Text, Boolean, Float, DateTime
import sqlalchemy
from .base import metadata


sat_token = sqlalchemy.Table(
    "sat_token",
    metadata,
    Column("token_sk", Integer, ForeignKey("hub_token.token_sk", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True),
    Column("name_owner", String(50), nullable=False),
    Column("email_owner", String(50), nullable=False),
    Column("date_create", DateTime, nullable=False, default=datetime.datetime.utcnow)
)