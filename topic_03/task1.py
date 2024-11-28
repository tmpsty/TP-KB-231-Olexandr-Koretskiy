def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Error: Division by zero"

while True:
    op = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
    if op == "exit":
        break
    a, b = float(input("First number: ")), float(input("Second number: "))
    print("Result:", calculate(a, b, op))
