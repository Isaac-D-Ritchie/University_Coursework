"""
Isaac Ritchie
Programming 2 - Test 1 - Prep 3

Design a student grading display system (Task propmpted by chatgpt)

The application must allow a user to:
    ● Record individual student assessment results
    ● View all stored student records in a structured format
    ● Calculate statistics over stored data
    ● Classify students based on performance
    ● Filter records based on defined criteria

For each student, store:
    ● Student Name (string)
    ● Subject (string)
    ● Score (0–100, integer)
    ● Assessment Type (e.g., Exam, Coursework, Test)

The application must operate entirely via the console and must repeatedly prompt
the user for actions until they choose to exit the program
"""


def safe_input(prompt: str) -> str:
    """
    Function to get a safe user input
    Arguments:
        prompt - for input question
    """
    try:
        raw_input = input(prompt)
        return raw_input
    except (KeyboardInterrupt, EOFError):
        return ""
    

def get_non_empty_string(prompt: str) -> str:
    """
    Function to get a non-empty valid sting
    Arguments:
        prompt - for input question
    Retunrs:
        Non-empty string
    """
    while True:
        try:
            raw_input: str = safe_input(prompt)
            sanitized_input: str = raw_input.strip()
            if sanitized_input == "":
                raise ValueError
            else:
                return sanitized_input

        except ValueError:
            print("Error: Invalid input")
            continue


def get_valid_int(prompt: str, min = None, max = None) -> int:
    """
    Funtion to get a valid integer input from the user
    Arguments:
        prompt - for input question
        min - for min input value
        max - for max input value
    Returns:
        valid integer value

    """
    while True:
        try:
            raw_input: str = safe_input(prompt)
            sanitized_input: int = int(raw_input.strip())

            if max is not None and sanitized_input > max:
                print(f"Error: Value must be <= {max}")
                continue
            elif min is not None and sanitized_input < min:
                print(f"Error: Value must be >= {min}")
            else:
                return sanitized_input

        except ValueError:
            print("Error: invalid input")
            continue


def get_choice(choices: list) -> str:
    """
    Function to get a valid user choice from given options
    Arguments:
        choices - given options for user to chooose from
    Returns:
        users coice
    """
    lowercase_choices = {c.lower(): c for c in choices}
    display_options = " - ".join(choices)

    while True:
        choice = get_non_empty_string(f"Choose from {display_options}")
        try:
            if choice.lower() in lowercase_choices:
                break
            else:
                raise ValueError
            
        except ValueError:
            print("Error: invalid choice")
            continue

    return lowercase_choices[choice]


def confirm_choice() -> bool:
    while True:
        input = safe_input("Confirm (Y//N): ").lower()
        if input == "y":
            return True
        elif input == "n":
            return False
        else:
            print("Error: Invalid input")
            continue


def add_entry(data: list[dict]) -> list[dict]:
    while True:
        entry_name = get_non_empty_string("Student Name: ")
        subject = get_non_empty_string("Subject: ")
        score = get_valid_int("Score", 0, 100)
        exam_type = get_choice(["Exam", "Coursework", "Test"])
        if score < 40:
            grade = "Fail"
        elif score > 40 and score <= 60:
            grade = "Pass"
        elif score >= 60 and score <= 75:
            grade = "Merit"
        elif score >= 75:
            grade = "Distinction"

        new_entry: dict = {"student_name": entry_name, "subject": subject,
                            "score": score, "exam_type": exam_type, "grade": grade}
        print(new_entry)
        confirm = confirm_choice()
        if confirm == False:
            continue
        elif confirm == True:
            break
        
        data.append(new_entry)
        return data


def view_all(data: list[dict]) -> None:
    """
    Funtion to print all data points
    Arguments:
        data -  to be displayed
    """
    if not data:
        print("Error: No data entrys")
        return
    
    for i in data:
        print(i)
    return


def view_by_grade(data: list[dict]) -> None:
    grade_choice = get_choice("Fail", "Pass", "Merit", "Distinction")
    for i in data:
        if i["Grade"] == grade_choice:
            print(i)
        else:
            continue
    return


def display_menu(data: list[dict]) -> None:
    """
    funtion to display menu text and get user menu choice
    Arguments:
        data - to be displayed through menu
    """
    while True:
        print(
            "\n--- Menu ---\n"
            "1. Add entry\n"
            "2. View all grades\n"
            "3. view by grade\n"
            "4. Quit")
        
        choice: int = get_valid_int("Enter option by (1-4)", 1, 4)

        if choice == 1:
            data = add_entry(data)
            safe_input("Enter any key to continue: ")
        elif choice == 2:
            view_all(data)
            safe_input("Enter any key to continue: ")
        elif choice == 3:
            view_by_grade(data)
            safe_input("Enter any key to continue: ")
        elif choice == 4:
            break


def main():
    print("Starting Grade Sytstem...")
    data = []
    display_menu(data)


if __name__ == "__main__":
    main()