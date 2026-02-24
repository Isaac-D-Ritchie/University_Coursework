"""
26708965 - Isaac Ritchie
Programming 2 - CW1 Task 1

Task:
You are required to design and implement a command-line-based Fitness
Tracking Application using the Python programming language. 
The application must operate entirely via the console and must repeatedly
prompt the user for actions until they choose to exit the program.

"""

def safe_input(prompt: str) -> str:
    """
    Function to get safe user input
    Args:
        prompt - for input question
    Returns:
        Valid input or empty string
    """
    try:
        raw_input = input(prompt)
        return raw_input
    except (KeyboardInterrupt, EOFError):
        print("Error: Invalid input (safe input)")
        return ""


def get_non_empty_string(prompt: str) -> str:
    """
    Function to get non empty string
    Args:
        prompt - for input question
    Retunrs:
        Non-empty string value
    """
    while True:
        try:
            raw_input = safe_input(prompt)
            sanitized_input: str = raw_input.strip()

            if sanitized_input == "":
                raise ValueError
            else:
                break

        except ValueError:
            print("Error: Invalid input")

    return sanitized_input


def get_valid_integer(prompt: str, min = None, max = None) -> int:
    """
    Function to get a valid integr within a given range (optional)
    Args:
        prompt - for input question
    Returns:
        Valid integr
    """
    while True:
        try:
            raw_input = safe_input(prompt)
            sanitized_input = int(raw_input.strip())

            if min is not None and sanitized_input < min:
                print("Error: Value too low")
            elif max is not None and sanitized_input > max:
                print("Error: Value too high")
            else:
                break

        except ValueError:
            print("Error: Invalid input")
            continue

    return sanitized_input


def get_valid_date() -> str:
    """
    Function to get date as (YYYY-MM-DD)
    Returns:
        Date as sting
    """
    while True:
        year = get_valid_integer("Enter year (YYYY): ",1950, 2100)
        month = get_valid_integer("Enter month (MM): ", 1, 12)
        date = get_valid_integer("Enter date (DD): ", 1, 31)
        full_date = f"{year}-{month:02}-{date:02}"

        while True:
            confirm = safe_input(f"Is {full_date} correct? (Y/N): ").lower()
            if confirm == "y":
                return full_date
            elif confirm == "n":
                break
            else:
                print("Error, invalid input")
                continue


def get_choice(choices: list) -> str:
    """
    Function to get a valid choice from given options
    Args:
        choices - given options
    Returns:
        Chosen option as string value
    """
    lowercase_choices = {c.lower(): c for c in choices}
    options = " - ".join(choices)

    while True:
        user_choice = (get_non_empty_string(
                        f"Enter choice from {options}: ")).lower()
        
        if user_choice in lowercase_choices:
            break
        else:
            print("Error: Invalid choice")
            continue

    return lowercase_choices[user_choice]


def add_workout(data: list[dict]) -> list[dict]:
    while True:
        workout_name = get_non_empty_string("Workout name: ")
        workout_date = get_valid_date()
        workout_cat = get_choice(["Cardio","Strength","Flexibility","Sport"])
        workout_time = get_valid_integer("Enter workout length seconds: ", 1, 9999)
        workout_entry = {"Date": workout_date,
                        "Name": workout_name,
                        "Category": workout_cat,
                        "Time": workout_time}

        entry_in_text = (f"Date: {workout_date} Name: {workout_name} "
                        f"Cat: {workout_cat} Time: {workout_time} Seconds")
        while True:
            confirm = safe_input(f"{entry_in_text}\nConfirm workout? (Y/N): ").lower()
            if confirm == "y":
                return workout_entry
            elif confirm == "n":
                break
            else:
                print("Error, invalid input")
                continue


def view_all(data: list[dict]) -> None:
    if not data:
        print("Error: No workouts recorded")
        return
    total_time = 0
    for i in data:
        print("\nDate           Name      Category    Time")
        print("-------------------------------------------")
        print(
            f"{i["Date"]:13}  {i["Name"]:8}  {i["Category"]:10}  {i["Time"]}")
        total_time += i["Time"]
    print(f"\nTotal workout time = {total_time} Seconds")
    return
        

def view_by_cat(data: list[dict]) -> None:
    """
    Function to display specific workouts, sorted by category
    Args:
        data - current saved workouts
    """
    if not data:
        print("Error: No workouts recorded")
        return
    
    specific_list = []
    total_time = 0
    cat_choice = get_choice(["Cardio","Strength","Flexibility","Sport"])
    
    for i in data:
        if i["Category"] == cat_choice:
            specific_list.append(i)
            print("\nDate           Name      Category    Time")
            print("-------------------------------------------")
            print(
                f"{i["Date"]:13}  {i["Name"]:8}  {i["Category"]:10}  {i["Time"]}")
            total_time += i["Time"]
        continue

    if not specific_list:
        print("Error: No workouts recorded")
        return
    
    print(f"\nTotal workout time = {total_time} Seconds")
    return



def display_menu(data: list[dict]) -> None:
    """
    Function to display menu and get menu choice
    Args:
        data - existing list of workouts
    """
    while True:
        print(
            "\n--- Fitness Tracker ---\n"
            "1. Add a workout\n"
            "2. View all workouts\n"
            "3. View specific workouts\n"
            "4. Quit"
        )

        menu_choice = get_valid_integer("Select menu option (1-4): ", 1, 4)
        if menu_choice == 1:
            data.append(add_workout(data))
            safe_input("Press any key to continue: ")
            continue
        if menu_choice == 2:
            view_all(data)
            safe_input("Press any key to continue: ")
        if menu_choice == 3:
            view_by_cat(data)
            safe_input("Press any key to continue: ")
        if menu_choice == 4:
            print("Closing fitness tracker...")
            break


def main():
    print("Launhing fitness tracker...")
    data = []
    view_all(data)
    display_menu(data)
    return

if __name__ == "__main__":
    main()