def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def find_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return f"Two real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        return "No real roots"

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

roots = find_roots(a, b, c)
print(roots)