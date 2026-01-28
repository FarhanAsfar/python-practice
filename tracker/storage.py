from .models import Expense
import json
import os

def create_expense():
    file_path = "./data/expenses.json"
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    expense1 = Expense(
        id=1,
        date="20206-01-28",
        category="food",
        amount=250.50,
        currency="BDT",
        note="lunch"
    )
    expense2 = Expense(
        id=2,
        date="20206-01-28",
        category="food",
        amount=250.50,
        currency="BDT",
        note="lunch"
    )

    print(expense1)

    # load existing data
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path)>0:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        else:
            data = []

        data.append(expense2.to_dict())

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Written to file {file_path} successfully")
    except IOError as e:
        print(f"Couldn't write to file: {e}")
