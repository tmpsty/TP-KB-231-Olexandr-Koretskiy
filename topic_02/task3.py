def calculate(a, b, operation):
    match operation:
        case "1" | "+": return a + b
        case "2" | "-": return a - b
        case "3" | "*": return a * b
        case "4" | "/": return a / b if b != 0 else "Error: Division by zero"
        case _: return "Invalid operation"

print("Welcome to the calculator!")
operation = input("Enter operation (1:+, 2:-, 3:*, 4:/): ")
a, b = float(input("First number: ")), float(input("Second number: "))
print(f"Result: {calculate(a, b, operation)}")