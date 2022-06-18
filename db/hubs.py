import datetime
from sqlalchemy.schema import Sequence
from sqlalchemy import CheckConstraint, ForeignKey, Column
from sqlalchemy import String, Integer, Text, Boolean, Float
import sqlalchemy
from .base import metadata


hub_token = sqlalchemy.Table(
    "hub_token",
    metadata,
    Column("token_sk", Integer, primary_key=True, autoincrement=True),
    Column("access_token", Text, unique=True, nullable=False),
    Column("refresh_token", Text, unique=True, nullable=False)
)
