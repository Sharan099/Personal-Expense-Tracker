import csv
from datetime import date


class Tracker:
    def add_expense(category, item, amount, expense_date=None):
        if expense_date is None:
            expense_date = date.today().strftime("%Y-%m-%d")
        
        # Open the CSV file in append mode
        with open("expenses_csv.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expense_date, category, item, amount])
        
        print(f"Expense added: {expense_date}, {category}, {item}, {amount}€")
