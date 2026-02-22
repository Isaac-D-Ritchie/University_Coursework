"""
Isaac Ritchie
Programming 2 - Test 1 - Prep 2

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

def safe_input(prompt):
    try:
        raw_input = input(prompt)
        return raw_input
    except (KeyboardInterrupt, EOFError) as e:
        print("Error: Invalid input")
        return""
    

def get_valid_string(prompt):
    while True:
        try:
            string_input = str(safe_input(prompt))

            if string_input == "":
                raise ValueError
            break
    
        except ValueError:
            print("Error: Invalid String")
            continue
        
    return string_input


def get_valid_int(prompt, min_value = None, max_value = None):
    while True:
        try:
            int_input = int(safe_input(prompt))

            if int_input == "":
                raise ValueError
            elif min_value is not None and int_input < min_value:
                raise ValueError
            elif max_value is not None and int_input > max_value:
                raise ValueError
            break
    
        except ValueError:
            print("Error: Invalid integer")
            continue
        
    return int_input
    

def get_valid_float(prompt, min_value = None, max_value = None):
    while True:
        try:
            float_input = float(safe_input(prompt))

            if float_input == "":
                raise ValueError
            elif min_value is not None and float_input < min_value:
                raise ValueError
            elif max_value is not None and float_input > max_value:
                raise ValueError
            break
    
        except ValueError:
            print("Error: Invalid float")
            continue

    return float_input

def view_all_expenses(expenses: list[dict]):
    if not expenses:
        print("Error: No cuurent expenses")
        return

    print("Date           Name       Price   Category")
    print("-------------------------------------------------")
    for i in expenses:
        print(f"{i["Date"]:14} {i["Expense"]:10} {i["Price"]:8} {i["Category"]} ")
    return


def get_valid_date():
    while True:
        day = get_valid_int("Enter day of the month (DD): ", 1, 31)
        month = get_valid_int("Enter month (MM): ", 1, 12)
        year = get_valid_int("Enter year (YYYY): ", 2000, 2050)
        full_date = f"{year}-{month:02}-{day:02}"

        confirmation = get_valid_string(f"Is {full_date} correct? (Y/N)").lower()
        if confirmation == "y":
            break
        elif confirmation == "n":
            continue
        else:
            continue

    return full_date


def get_choice(categorys):
    lowercase_cats = {c.lower(): c for c in categorys}
    options = " - ".join(categorys)

    while True:
        choice = get_valid_string("Enter category:").lower()

        if choice in lowercase_cats:
            print(choice)
            return lowercase_cats[choice]
        else:
            print("Error: Invalid catagory\n"
                  f"Please choose from {options}")
            continue


def add_expense(expenses, expense_cats):
    name = get_valid_string("Enter expense name: ")
    price = f"£{get_valid_float("Enter expense price: ", 0, 9999):.2f}"
    date = get_valid_date()
    category = get_choice(expense_cats)
    new_expense = {"Expense": name,"Price": price, "Category": category, "Date": date}
    expenses.append(new_expense)
    return expenses


def view_specific_expense(expenses, expense_cats):
    choice = get_choice(expense_cats)
    if not expenses:
        print("Error: No cuurent expenses")

    print("Date           Name       Price   Category")
    print("-------------------------------------------------")
    for i in expenses:
        if i["Category"] == choice:
            print(f"{i["Date"]:14} {i["Expense"]:10} {i["Price"]:8} {i["Category"]} ")
        else:
            continue




def display_menu():
    print(
        "\n-- Expense Tracker --\n"
        "1. Add expenses\n"
        "2. View all expenses\n"
        "3. View specific expenses\n"
        "4. Quit\n"
    )


def main():
    expenses = []
    expense_categories = ["Food","Transport","Utilities","Entertainment","Other"]

    while True:
        display_menu()
        menu_choice = get_valid_int("Enter menu choice: ", 1, 4)

        if menu_choice == 1:
            expenses = add_expense(expenses, expense_categories)

        elif menu_choice == 2:
            view_all_expenses(expenses)

        elif menu_choice == 3:
            view_specific_expense(expenses, expense_categories)

        elif menu_choice == 4:
            print("Closing Program")
            break

        safe_input("Enter any key to continue")



if __name__ == "__main__":
    main()