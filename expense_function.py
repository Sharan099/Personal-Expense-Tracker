import csv
from datetime import date
from collections import defaultdict

FILENAME = "expenses.csv"

class Tracker:
    @staticmethod
    def add_expense(expense_date=None):
        if expense_date is None:
            expense_date = date.today().strftime("%Y-%m-%d")

        category = input("Enter category: ")
        item = input("Enter Item name: ")
        amount = float(input("Enter the amount in EUR: "))
        
        # ✅ use expense_date (not date)
        return {"date": expense_date, "category": category, "item": item, "amount": amount}

    @staticmethod
    def save_to_csv(expense):
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "category", "item", "amount"])
            # ✅ write header only if file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(expense)

    @staticmethod
    def show_all_expenses():
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    @staticmethod
    def show_expenses_by_category():
        categories = defaultdict(list)
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                categories[row["category"]].append(row)

        for category, items in categories.items():
            print(f"\n=== {category.upper()} ===")
            for item in items:
                print(f"{item['date']} | €{item['amount']} | {item['item']}")

    @staticmethod
    def show_total_expenses():
        total = 0
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # ✅ ensure amount key exists and is numeric
                if "amount" in row and row["amount"]:
                    total += float(row["amount"])
        print(f"\n💰 Total Expenses: €{total:.2f}")
