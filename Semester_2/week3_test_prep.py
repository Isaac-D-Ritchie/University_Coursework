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
        
def load_inventory(inventory: list[dict]) -> None:
    try:
        with open ("test_prep_inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
            return
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return
        
        
if __name__ == "__main__":
    float = get_valid_float("Enter float", 0, 10)
    print(float)
    string = get_non_empty_string("Enter non empty string")
    print(string)

    inventory_test = [{"Name": "isaac", "Price": 20}, {"Name": "anna", "Price": 50}]
    load_inventory(inventory_test)