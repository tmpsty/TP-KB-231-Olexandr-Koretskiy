actions = ["(", "+", "-", "*", "/", "^", ")"]

def get_priority(operator):
    match actions.index(operator):
        case 0:
            return 0
        case 1 | 2:
            return 1
        case 3 | 4:
            return 2
        case 5:
            return 3

def to_rpn(expression):

    tokens = expression.split()
    stack = []
    rpn_expression = []

    for token in tokens:
        if token in actions:
            if token == actions[0]:  
                stack.append(token)

            elif token == actions[6]:  
                while stack and stack[-1] != actions[0]:
                    rpn_expression.append(stack.pop())
                stack.pop()

            elif stack and get_priority(stack[-1]) >= get_priority(token):
                rpn_expression.append(stack.pop())
                stack.append(token)

            else:
                stack.append(token)
        else:
            rpn_expression.append(token)

    rpn_expression.extend(reversed(stack))
    return rpn_expression

def evaluate_rpn(rpn):
   
    stack = []

    for token in rpn:
        if token in actions:
            a = float(stack.pop())
            b = float(stack.pop())
            match token:
                case "+":
                    stack.append(b + a)
                case "-":
                    stack.append(b - a)
                case "*":
                    stack.append(b * a)
                case "/":
                    stack.append(b / a)
                case "^":
                    stack.append(b ** a)
        else:
            stack.append(token)

    return stack[0]

if __name__ == "__main__":
    expression = input("Enter your expression: ")
    print(f"Default sequence: {expression}")

    rpn_sequence = to_rpn(expression)
    rpn_string = " ".join(rpn_sequence)
    print(f"Reverse Polish notation: {rpn_string}")

    result = evaluate_rpn(rpn_sequence)
    print(f"Answer: {result}")
