from sqlalchemy import Table, Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.db import metadata

transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("amount", Float, nullable=False),
    Column("type", String, nullable=False),  
    Column("category", String, nullable=False),
    Column("description", String),
    Column("date", DateTime, default=datetime.utcnow),
)
