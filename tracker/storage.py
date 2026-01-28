from .models import Expense
import json


def create_expense():
    expense1 = Expense(
    id=1,
    date="20206-01-28",
    category="food",
    amount=250.50,
    currency="BDT",
    note="lunch"
    )

    print(expense1)