from operations import perform_operation

def main():
    print("Calculator")
    print("Operation: +, -, *, /")
    
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        if operation.lower() == "exit":
            print("Work completed.")
            break
        try:
            result = perform_operation(operation)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
