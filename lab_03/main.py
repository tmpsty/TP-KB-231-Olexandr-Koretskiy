from Student import Student
from StudentList import StudentList
from Utils import FileInOut

DEF_NAME = r"TP-KB-231-Olexandr-Koretskiy\lab_03\lab3.csv"

def main():
    file_io = FileInOut()
    student_list = StudentList(file_io.import_data(DEF_NAME))

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match choice:
            case "C" | "c":
                name = input("Enter name: ") or "Unknown"
                phone = input("Enter phone: ") or "Unknown"
                group = input("Enter group: ") or "Unknown"
                email = input("Enter email: ") or "Unknown"
                student = Student(name=name, phone=phone, group=group, email=email)
                student_list.addNewElement(student)
            case "U" | "u":
                name = input("Enter name to update: ")
                index = student_list.findElement(name)
                if index == -1:
                    print("Student not found")
                    continue
                current = student_list.students[index]
                print(f"Current: {current}")
                new_name = input("Enter new name (or press Enter to skip): ") or current.name
                new_phone = input("Enter new phone (or press Enter to skip): ") or current.phone
                new_group = input("Enter new group (or press Enter to skip): ") or current.group
                new_email = input("Enter new email (or press Enter to skip): ") or current.email
                updated_student = Student(new_name, new_phone, new_group, new_email)
                student_list.updateElement(index, updated_student)
            case "D" | "d":
                name = input("Enter name to delete: ")
                student_list.deleteElement(name)
            case "P" | "p":
                student_list.printAllList()
            case "X" | "x":
                file_io.save_data(DEF_NAME, student_list.students)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
