from functions import add, subtract, multiply, divide

def get_numbers():
    while True:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            return a, b
        except ValueError:
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
