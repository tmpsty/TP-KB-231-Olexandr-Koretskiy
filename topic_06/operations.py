from functions import add, subtract, multiply, divide
from log import log_action

def get_numbers():
    while True:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            log_action("Input", f"First number: {a}, Second number: {b}")
            return a, b
        except ValueError:
            log_action("Error", "Invalid number input")
            print("Error: please enter correct numbers!")

def perform_operation(operation):
    a, b = get_numbers()
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        raise ValueError("Unknown operation!")
