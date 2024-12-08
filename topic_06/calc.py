import os
from operations import perform_operation

# Функція для запису логів у файл
def log_action(action, details):
    log_file = os.path.join("log.txt")  # Лог-файл буде створено в поточній папці (topic_06)
    with open(log_file, "a") as file:
        file.write(f"{action}: {details}\n")

def main():
    print("Calculator")
    print("Operation: +, -, *, /")
    
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        if operation.lower() == "exit":
            log_action("Program Termination", "User exited the program.")
            print("Work completed.")
            break
        try:
            result = perform_operation(operation)
            log_action("Operation", f"Operation: {operation}, Result: {result}")
            print(f"Result: {result}")
        except ValueError as e:
            log_action("Error", f"Operation: {operation}, Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            log_action("Unexpected Error", f"Operation: {operation}, Error: {e}")
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
