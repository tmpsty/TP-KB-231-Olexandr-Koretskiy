# Початковий список словників
students = [
    {"name": "Alex", "grade": 85},
    {"name": "Alex1", "grade": 92},
    {"name": "Alex2", "grade": 78},
    {"name": "Alex3", "grade": 88},
    {"name": "Alex4", "grade": 95}
]

# Сортування за іменем
sorted_by_name = sorted(students, key=lambda student: student["name"])
print("Sorted by name:")
print(sorted_by_name)

# Сортування за оцінкою
sorted_by_grade = sorted(students, key=lambda student: student["grade"])
print("\nSorted by grade:")
print(sorted_by_grade)
