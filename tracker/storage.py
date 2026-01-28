from .models import Expense
import json
import os

def create_expense(expense_data):
    file_path = "./data/expenses.json"
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # expense1 = Expense(
    #     id=1,
    #     date="20206-01-28",
    #     category="food",
    #     amount=250.50,
    #     currency="BDT",
    #     note="lunch"
    # )
    # expense2 = Expense(
    #     id=2,
    #     date="20206-01-28",
    #     category="food",
    #     amount=250.50,
    #     currency="BDT",
    #     note="lunch"
    # )

    # print(expense1)

    # # load existing data
    # try:
    #     if os.path.exists(file_path) and os.path.getsize(file_path)>0:
    #         with open(file_path, 'r') as json_file:
    #             data = json.load(json_file)
    #     else:
    #         data = []

    #     data.append(expense2.to_dict())

    #     with open(file_path, 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #     print(f"Written to file {file_path} successfully")
    # except IOError as e:
    #     print(f"Couldn't write to file: {e}")

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict): data = [data]
    else:
        data = []

    # 2. Auto-generate ID (Max ID + 1)
    new_id = max([item.get('id', 0) for item in data], default=0) + 1
    expense_data['id'] = new_id

    # 3. Append and Write
    data.append(expense_data)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"ID: {new_id} added successfully.")
