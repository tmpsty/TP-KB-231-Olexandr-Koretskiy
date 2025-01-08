act = ["(", "+", "-", "*", "/", "^", ")"]

def priority(action):
    match act.index(action):
        case 0:
            return 0
        case 1 | 2:
            return 1
        case 3 | 4:
            return 2
        case 5:
            return 3

def Stage1(expression):
    exp_elem = expression.split()
    stack = []
    S1exp = []
    for elem in exp_elem: 
        if elem in act:
            if elem == act[0]:
                stack.append(elem)

            elif elem == act[6]:
                while stack[-1] != act[0]:
                    S1exp.append(stack.pop(-1))
                stack.pop(-1)

            elif len(stack) != 0 and priority(stack[-1]) >= priority(elem):
                S1exp.append(stack.pop(-1))
                stack.append(elem)

            else:
                stack.append(elem)
        else:
            S1exp.append(elem)

    S1exp.extend(stack[::-1])
    return S1exp
    

def Stage2(RPN):
    ans_list = []
    for elem in RPN:
        if elem in act:
            a = float(ans_list.pop(-1))
            b = float(ans_list.pop(-1))
            match elem:
                case "+":
                    ans_list.append(b + a)
                case "-":
                    ans_list.append(b - a)
                case "*":
                    ans_list.append(b * a)
                case "/":
                    ans_list.append(b / a)
                case "^":
                    ans_list.append(b ** a)
        else:
            ans_list.append(elem)
    return ans_list[0]

if __name__ == "__main__":
    def_str = input("Enter your expression: ")
    print(f"Default sequence: {def_str}")

    S1sequence = Stage1(def_str)
    RPN_str = ""
    for elem in S1sequence:
        RPN_str += f"{elem} "
    print(f"Reverse Polish notation: {RPN_str}")
    
    ans = Stage2(S1sequence)
    print(f"Answer: {ans}")