class StudentList:
    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = students

    def addNewElement(self, student_add):
        insert_position = 0
        for item in self.students:
            if student_add.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student_add)
        print("New element has been added")

    def findElement(self, name):
        for index, item in enumerate(self.students):
            if item.name == name:
                return index
        return -1

    def deleteElement(self, name):
        index_delete = self.findElement(name)
        if index_delete != -1:
            self.students.pop(index_delete) 
            print("The student was deleted")
        else:
            print("Element was not found")

    def updateElement(self, index, new_data):
        if 0 <= index < len(self.students):
            current = self.students[index]
            if (
                current.name == new_data.name
                and current.phone == new_data.phone
                and current.group == new_data.group
                and current.email == new_data.email
            ):
                print("You haven't updated student information")
            else:
                self.students[index] = new_data
                print("Information has been updated")
        else:
            print("Invalid index")

    def printAllList(self):
        if not self.students:
            print("The list of students is empty.")
        else:
            for student in self.students:
                print(student)
