from pydantic import BaseModel

class Expense(BaseModel):
    id: int
    date: str
    category: str
    amount: float
    currency: str
    note: str
    