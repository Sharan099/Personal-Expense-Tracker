from expense_function import Tracker
import currency_conv_api

import pandas as pd 

command = ""


print("Welcome to the expense tracker")

user = input("Enter the user name \n")

print(f"Welcome {user} !")

print(""" Enter 
    1.Add Expenses
    2.view all Expenses
    3.view by category
    4.show summary
    5.View Expense in INR
    6.Exit""")


while command.lower() != "6":
    command=input(">").lower()

    if command == "1":
        expense = Tracker.add_expense()
        Tracker.save_to_csv(expense)

    elif command=="2":
        Tracker.show_total_expenses()
    
    elif command=="3":
        Tracker.show_expenses_by_category()
    elif command=="4":
        Tracker.show_all_expenses()
    elif command=="5":
        total = Tracker.show_total_expenses()
        currency_conv_api.convert_currency(total)

        

        


        
        
        
