"""
week 3 test prep>

This test is to create a functioning expense tracker
"""
import json

"""Reuseable functions prep"""

def safe_input(prompt: str) -> str:
    try:
        safe_input = input(prompt)
        return safe_input
    except (KeyboardInterrupt, EOFError):
        return ""
    

def get_non_empty_string(prompt: str) -> str:
    while True:
            raw_input = safe_input(prompt)
            sanitized_input = raw_input.strip()
            if sanitized_input == "":
                 print("Error: empty input")
                 continue
            else:
                 return sanitized_input
            

def get_valid_float(prompt: str, min_range = None, max_range = None) -> float:
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip()
        try:
            float_input = float(sanitized_input)

            if min_range is not None and float_input < min_range:
                print(f"Error: value must be more than {min_range}")
                continue
            if max_range is not None and float_input > max_range:
                print(f"Error: value must be less than {max_range}")
                continue
                 
            return float_input
        except ValueError:
               print("Error: invalid float input")
               continue
        
def get_valid_integer(prompt:str, min_range = None, max_range = None) -> int:
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip()
        try:
            int_input = int(sanitized_input)

            if min_range is not None and int_input < min_range:
                print(f"Error: value must be more than {min_range}")
                continue
            if max_range is not None and int_input > max_range:
                print(f"Error: value must be less than {max_range}")
                continue

            return int_input
        except ValueError:
               print("Error: invalid float input")
               continue

def load_inventory(inventory: list[dict]) -> None:
    try:
        with open ("test_prep_inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
            return
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return
        

def get_valid_date() -> str:
     while True:
        year = get_valid_integer("Enter year (YYYY): ", 1900, 2099)
        month = get_valid_integer("Enter month (MM):", 1, 12)
        day = get_valid_integer("Enter day (DD):", 1, 31)
        full_date = f"{year}-{month:02}-{day:02}"
        
        while True:
            confirmation = safe_input(f"Is {full_date} correct? (Y/N)").strip()
            if confirmation == "y":
                return full_date
            if confirmation == "n":
                break
            else:
                print("Invalid input, try Y or N")
                continue
            get_valid_date()

              
def get_valid_choice(prompt, choices: list[str]) -> str:
    lowercase_options = {c.lower(): c for c in choices}
    while True:
        raw_input = safe_input(prompt)
        sanitized_input = raw_input.strip().lower()

        if sanitized_input == "":
            print("Error: Input cannot be empty")
            continue

        if sanitized_input not in lowercase_options:
            options = " - ".join(choices)
            print(f"Error: Please select from {options}")
            continue

        return lowercase_options[sanitized_input]



if __name__ == "__main__":
    choice = get_valid_choice("Enter category: ", ["One", "Two", "Three"])
    print(choice)

    date = get_valid_date()
    print(date)

    float = get_valid_float("Enter float", 0, 10)
    print(float)
    string = get_non_empty_string("Enter non empty string")
    print(string)

    inventory_test = [{"Name": "isaac", "Price": 20}, {"Name": "anna", "Price": 50}]
    load_inventory(inventory_test)