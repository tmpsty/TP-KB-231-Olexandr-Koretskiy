def calculate(a, b, operation):
    if operation in ("1", "+"):
        return a + b
    elif operation in ("2", "-"):
        return a - b
    elif operation in ("3", "*"):
        return a * b
    elif operation in ("4", "/"):
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

print("Welcome to the calculator!")
operation = input("Enter operation (1:+, 2:-, 3:*, 4:/): ")
a, b = float(input("First number: ")), float(input("Second number: "))
print(f"Result: {calculate(a, b, operation)}")