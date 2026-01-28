from pydantic import BaseModel

class Expense(BaseModel):
    id: int
    date: str
    category: str
    amount: float
    currency: str
    note: str
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "currency": self.currency,
            "note": self.note
        }