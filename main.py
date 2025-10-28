from expense_function import Tracker

command = ""


print("Welcome to the expense tracker")
user = input("Enter the user name \n")
print(f"Welcome {user} !")
print(""" Enter 
    1.Add Expenses
    2.view all Expenses
    3.view by category
    4.show summary
    5.Exit""")
while command.lower() != "5":
    command=input(">").lower()

    if command == "1":
        category = input("Enter category\n")
        item = input("Enter Item name\n")
        amount = input("Enter the amount in EUR\n")
        Tracker.add_expense(category,item,amount)
        print("Expense added sucessfully")

        


        
        
        
