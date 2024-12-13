from functions import OperationsTest

class Calculator:
    def __init__(self):
        self.operations = OperationsTest()

    def get_numbers(self):
        while True:
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                return a, b
            except ValueError:
                print("Error: please enter correct numbers!")

    def perform_operation(self, operation):
        a, b = self.get_numbers()
        if operation == "+":
            return self.operations.add(a, b)
        elif operation == "-":
            return self.operations.subtract(a, b)
        elif operation == "*":
            return self.operations.multiply(a, b)
        elif operation == "/":
            return self.operations.divide(a, b)
        else:
            raise ValueError("Unknown operation!")
