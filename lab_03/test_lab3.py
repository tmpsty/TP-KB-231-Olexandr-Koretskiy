import unittest
import unittest.mock
from io import StringIO
import sys
import os
import tempfile
import csv

from Student import Student
from StudentList import StudentList
from Utils import FileInOut

class TestStudentSystem(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile('w', encoding='utf-8', newline='', delete=False)
        self.test_file_name = self.test_file.name
        self.test_file.close()
        self.student_list = StudentList()
        self.file_io = FileInOut()

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_student_creation(self):
        student = Student(name="Test", phone="0661234567", group="KB-231", email="test@example.com")
        self.assertEqual(student.name, "Test")
        self.assertEqual(student.phone, "0661234567")
        self.assertEqual(student.group, "KB-231")
        self.assertEqual(student.email, "test@example.com")

    def test_add_new_element(self):
        student = Student(name="Test", phone="0661234567", group="KB-231", email="test@example.com")
        self.student_list.addNewElement(student)

        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Test")

    def test_delete_element(self):
        student = Student(name="Test", phone="0661234567", group="KB-231", email="test@example.com")
        self.student_list.addNewElement(student)

        self.student_list.deleteElement("Test")
        self.assertEqual(len(self.student_list.students), 0)

        self.student_list.deleteElement("NonExistent")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_element(self):
        student = Student(name="Test", phone="0661234567", group="KB-231", email="test@example.com")
        self.student_list.addNewElement(student)

        updated_student = Student(name="Test", phone="0669999999", group="KB-232", email="updated@example.com")
        self.student_list.updateElement(0, updated_student)

        self.assertEqual(self.student_list.students[0].name, "Test")
        self.assertEqual(self.student_list.students[0].phone, "0669999999")
        self.assertEqual(self.student_list.students[0].group, "KB-232")
        self.assertEqual(self.student_list.students[0].email, "updated@example.com")

        self.student_list.updateElement(0, updated_student)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Test")

    def test_print_all_list(self):
        student = Student(name="Test", phone="0661234567", group="KB-231", email="test@example.com")
        self.student_list.addNewElement(student)

        captured_output = StringIO()
        sys.stdout = captured_output
        self.student_list.printAllList()
        sys.stdout = sys.__stdout__

        self.assertIn("Test", captured_output.getvalue())
        self.assertIn("KB-231", captured_output.getvalue())

    def test_import_data(self):
        data = [
            {"name": "Alex", "phone": "0631234567", "group": "KB-231", "email": "bob@example.com"},
            {"name": "Jon", "phone": "0631234567", "group": "KB-234", "email": "jon@example.com"}
        ]
        with open(self.test_file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "group", "email"])
            writer.writeheader()
            writer.writerows(data)

        students = self.file_io.import_data(self.test_file_name)

        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "Alex")
        self.assertEqual(students[1].email, "jon@example.com")

    def test_save_data(self):
        students = [
            Student(name="Chris", phone="0667777777", group="KB-232", email="chris@example.com")
        ]
        self.file_io.save_data(self.test_file_name, students)

        with open(self.test_file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Chris")
            self.assertEqual(rows[0]["email"], "chris@example.com")

if __name__ == '__main__':
    unittest.main()
