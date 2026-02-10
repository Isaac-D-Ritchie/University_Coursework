"""
Isaac Ritchie - 26708965
Programming 2 - Test 1

Design and implement a command-line-based expense Tracking
Application using the Python programming language.

The application must allow a user to:
    ● Record individual expense entries
    ● View stored expense data in a structured format
    ● Perform basic calculations over the stored data
    ● Filter expense records based on defined criteria

The application must operate entirely via the console and must repeatedly prompt
the user for actions until they choose to exit the program
"""

"""Functions"""
def safe_input(prompt: str) -> str:
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except (KeyboardInterrupt, EOFError):
            return ""


def get_valid_string(prompt: str) -> str:
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip()

        if sanitized_input == "":
            print("Error: No input provided")
            continue
        
        return sanitized_input


def get_valid_integer(prompt: str, min_value: int = None, max_value: int = None) -> int:
    while True:
        try:
            raw_input = safe_input(prompt)
            sanitized_input = raw_input.strip()
            int_value = int(sanitized_input)

            if min_value is not None and int_value < min_value:
                print(f"Error: Value must be above {min_value}")
                continue
            if max_value is not None and int_value > max_value:
                print(f"Error: Value must be below {max_value}")
                continue
            return int_value
        
        except ValueError:
            print("Error: Invalid integer")
            continue


def get_valid_price(prompt: str, min_value = None, max_value = None) -> float:
    while True:
        try:
            raw_input = safe_input(prompt)
            sanitized_input = raw_input.strip()
            float_value = float(sanitized_input)

            if min_value is not None and float_value < min_value:
                print(f"Error: Value must be {min_value} or below")
                continue
            if max_value is not None and float_value > max_value:
                print(f"Error: Value must be {max_value} or below")
                continue
            return float_value
        
        except ValueError:
            print("Error: Invalid float number")
            continue


def get_valid_date() -> str:
    year = get_valid_integer("Enter year (YYYY): ", 1900, 2100)
    month = get_valid_integer("Enter month (MM): ", 1, 12)
    day = get_valid_integer("Enter day (DD): ", 1, 31)
    full_date = f"{year}-{month:02}-{day:02}"
    while True:
        confirmation = safe_input(f"Is {full_date} correct (y/n)").lower()
        if confirmation == "y":
            return full_date
        if confirmation == "n":
            break
        else:
            print("Invalid Input, try Y or N")
            continue

        get_valid_date()


def get_valid_choice(choices: list[str]) -> str:
    lowercase_options = {c.lower(): c for c in choices}
    options = " - ".join(choices)

    while True:
        raw_input = safe_input(f"Enter a choice from {options}")
        sanitized_input = raw_input.strip().lower()

        if sanitized_input == "":
            print("Error: No input")
            continue
        
        if sanitized_input not in lowercase_options:
            print(f"Error: Please chose from {options}")
            continue

        return lowercase_options[sanitized_input]
    
def add_expense(expenses: list[dict], categories: list[str]) -> list[dict]:
    expense_date = get_valid_date()
    expense_name = get_valid_string("Enter expense name: ")
    expense_price = get_valid_price("Enter expense price: ")
    expense_category = get_valid_choice(categories)
    new_expense = {"date": expense_date,"name":expense_name,"price":expense_price,"cat":expense_category}
    
    expenses.append(new_expense)
    return expenses



def menu_features(choice: int, expenses_input: list[dict]) -> None:
    expense_categories = ["Food","Transport","Utilities","Entertainment","Other"]
    expenses = expenses_input

    if choice == 1:
        total = 0
        if not expenses:
            print("No current expenses")
        for expense in expenses:
            print(expense)
            total += expense['price']
            print(f"total = {total}")

        print(total)
        done = safe_input("Press any key to continue")
        return expenses
    
    if choice == 2:
        choice = get_valid_choice(expense_categories)
        total = 0
        if not expenses:
            print("No current expenses")
        for expense in expenses:
            if expense["cat"] == choice:
                print(expense)
                total += expense['price']
                print(f"total = {total}")
        done = safe_input("Press any key to continue")
        return expenses
    
    if choice == 3:
        new_expenses = add_expense(expenses, expense_categories) 

        done = safe_input("Press any key to continue")
        return new_expenses
        
    
def main() -> None:
    expenses = []
    while True:

        print("\nExpense tracker menu:\n"
              "1. View all expenses\n"
              "2. View expense by category\n"
              "3. Add expense\n"
              "4. Quit menu")
        menu_choice = get_valid_integer("\nPlease choose menu option:", 1, 4)
        if menu_choice == 4:
            print("Closing program")
            break
        else:
            expenses = (menu_features(menu_choice, expenses))




"""Start program"""
if __name__ == "__main__":
    main()