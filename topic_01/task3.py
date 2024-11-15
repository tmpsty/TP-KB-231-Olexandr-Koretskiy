def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = calculate_discriminant(a, b, c)

print("Discriminant:", discriminant)
