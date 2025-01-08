class Student:
    def __init__(self, name, phone, group, email):
        self.name = name
        self.phone = phone
        self.group = group
        self.email = email

    def __str__(self):
        return f"Student name is {self.name}, Phone is {self.phone}, Group is {self.group}, Email is {self.email}"
