def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        else:
            raise ValueError("Invalid operation.")
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

def get_user_input(prompt, input_type=float):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    op = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
    if op.lower() == "exit":
        break
    if op not in {"+", "-", "*", "/"}:
        print("Invalid operation. Please enter one of +, -, *, /.")
        continue

    a = get_user_input("First number: ")
    b = get_user_input("Second number: ")
    print("Result:", calculate(a, b, op))