"""
Semester 2 - Week 2 Lab

This labs challenge is to create an expense tracker application

Key objectives:
    # Store expense data using variables and dictionaries.
    # Validate user input (Defensive Programming).
    # Calculate totals and budgets.
    # Work with lists and string formatting
"""


def is_valid_category(cat):
    valid_categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]
    if cat in valid_categories:
        return True
    else:
        return False


def safe_input(prompt):
    try:
        return input(prompt).strip()

    except (KeyboardInterrupt, EOFError):
        return ("")
    

def get_valid_integer(prompt):
    while True:
        try:
            value_str = safe_input(prompt).strip()
            if not value_str:
                print("Input required")
            value_int = int(value_str)
            break
            return value_int
        
        except ValueError:
            print("Invalid input, try again")


def get_valid_positive_float(prompt):
    while True:
        try:
            value_str = safe_input(prompt).strip()
            if not value_str:
                print("Input required")
            value_float = float(value_str)
            if value_float < 0:
                raise ValueError
            return value_float
        
        except ValueError:
            print("Invalid input, try again")


def get_non_empty_string(prompt):
    while True:
        try:
            value_str = safe_input(prompt).strip()
            if not value_str:
                print("Input required")
            value = str(value_str)
            return value
        except ValueError:
            print("Invalid input, try again")


expenses: list[dict] = [{"expense_name": "tea", "Price": 2.25, "category": "Food"}]
while True:
    try:

        print("Current expenses:")
        for expense in expenses:
            print(f"\nname: {expense['expense_name']},\nprice: £{expense['Price']:.2f},\ncat: {expense['category']}\n")

        name = get_non_empty_string("Enter new expense name:")
        amount = get_valid_positive_float("Enter new expense price £:")

        record = {"expense_name": name, "Price": amount,"category": "Food"}
        expenses.append(record)
        print("Expense Added!")
        print("All expenses:")
        for expense in expenses:
            print(f"\nname: {expense['expense_name']},\nprice: £{expense['Price']:.2f},\ncat: {expense['category']}\n")

        total = 0
        for expense in expenses:
            total += expense["Price"]
        print(f"total expenses: £{total}")

    except ValueError:
        print("Error, try again")