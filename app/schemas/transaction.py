from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    amount: float
    type: str 
    category: str
    description: str = ""

class TransactionOut(TransactionIn):
    id: int
    date: datetime
