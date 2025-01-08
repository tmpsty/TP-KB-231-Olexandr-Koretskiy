import csv
from Student import Student

class FileInOut:
    def import_data(self, file_name):
        students = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row.get("name", "Unknown"),
                        phone=row.get("phone", "Unknown"),
                        group=row.get("group", "Unknown"),
                        email=row.get("email", "Unknown")
                    )
                    students.append(student)
        except FileNotFoundError:
            print(f"File '{file_name}' not found. The initial list will be empty.")
        except Exception as e:
            print(f"Error reading file: {e}")
        return students

    def save_data(self, file_name, students):
        students_str = [
            {"name": student.name, "phone": student.phone, "group": student.group, "email": student.email}
            for student in students
        ]
        try:
            with open(file_name, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["name", "phone", "group", "email"])
                writer.writeheader()
                writer.writerows(students_str)
            print(f"Data successfully saved to '{file_name}'")
        except Exception as e:
            print(f"Error saving file: {e}")
