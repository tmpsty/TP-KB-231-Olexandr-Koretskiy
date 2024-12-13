class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} age"

# Створення списку об'єктів класу Student
students = [
    Student("Alex", 21),
    Student("Oleg", 19),
    Student("Nikita", 22),
    Student("Anya", 20)
]

# Сортування списку за віком за допомогою lambda
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованого списку
for student in sorted_students:
    print(student)
