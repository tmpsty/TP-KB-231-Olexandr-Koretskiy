## Extended Student Directory with Sorting

# Sorted list of students
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "group": "CS101"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "group": "CS102"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@example.com", "group": "CS101"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@example.com", "group": "CS103"}
]

def print_all_students():
    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")

def add_new_student():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    group = input("Enter student group: ")
    new_student = {"name": name, "phone": phone, "email": email, "group": group}

    # Find the correct insert position to keep the list sorted
    insert_position = 0
    for student in students:
        if name > student["name"]:
            insert_position += 1
        else:
            break
    students.insert(insert_position, new_student)
    print("New student has been added.")

def delete_student():
    name = input("Enter the name of the student to delete: ")
    delete_position = next((i for i, student in enumerate(students) if student["name"] == name), -1)
    
    if delete_position == -1:
        print("Student not found.")
    else:
        del students[delete_position]
        print("Student has been deleted.")

def update_student():
    name = input("Enter the name of the student to update: ")
    student_index = next((i for i, student in enumerate(students) if student["name"] == name), -1)

    if student_index == -1:
        print("Student not found.")
    else:
        print("Current details:")
        print(f"Name: {students[student_index]['name']}, Phone: {students[student_index]['phone']}, Email: {students[student_index]['email']}, Group: {students[student_index]['group']}")

        new_name = input("Enter new name (leave blank to keep current): ") or students[student_index]['name']
        new_phone = input("Enter new phone (leave blank to keep current): ") or students[student_index]['phone']
        new_email = input("Enter new email (leave blank to keep current): ") or students[student_index]['email']
        new_group = input("Enter new group (leave blank to keep current): ") or students[student_index]['group']

        # Update the student details
        students[student_index] = {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
            "group": new_group
        }

        # Re-sort the list
        students.sort(key=lambda x: x["name"])
        print("Student information has been updated.")

def main():
    while True:
        choice = input("Choose an action [C: create, U: update, D: delete, P: print, X: exit]: ").lower()
        if choice == "c":
            add_new_student()
            print_all_students()
        elif choice == "u":
            update_student()
            print_all_students()
        elif choice == "d":
            delete_student()
            print_all_students()
        elif choice == "p":
            print_all_students()
        elif choice == "x":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
