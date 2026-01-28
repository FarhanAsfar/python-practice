import argparse
from .storage import create_expense

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # 'add' command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--note", default="")

    args = parser.parse_args()

    if args.command == "add":
        new_expense = {
            "date": args.date,
            "category": args.category,
            "amount": args.amount,
            "note": args.note,
            "currency": "BDT" # Defaulting for now
        }
        create_expense(new_expense)

if __name__ == "__main__":
    main()