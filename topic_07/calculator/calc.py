from operations import Calculator

def main():
    print("Calculator")
    print("Operation: +, -, *, /")
    
    calc = Calculator()
    
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        if operation.lower() == "exit":
            print("Work completed.")
            break
        try:
            result = calc.perform_operation(operation)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
