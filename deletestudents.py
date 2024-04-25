import tkinter as tk
from tkinter import messagebox
import csv

class DeleteStudent:
    def __init__(self, tree):
        self.tree = tree

    def delete_selected_student(self):
        selected_item = self.tree.focus() 
        if selected_item:
            student_data = self.tree.item(selected_item, 'values')
            student_name = student_data[0]
            student_code = student_data[2]

            confirm = messagebox.askyesno("Delete Student", f"Are you sure you want to delete {student_name}?")
            if confirm:
                self.remove_student_from_csv(student_code)
                messagebox.showinfo("Success", f"{student_name} has been deleted.")
                self.refresh_student_list()

    def remove_student_from_csv(self, student_code):
        students = []
        with open('students.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Student Code'] != student_code:
                    students.append(row)

        with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Date of Birth', 'Student Code', 'Class Code', 'ECTs', 'Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

    def refresh_student_list(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing data
        # Refresh student list after deletion
        from showstudents import ShowStudent  # Import inside function to avoid circular import
        show_student = ShowStudent(self.tree)
        show_student.refresh_student_list()


class DeleteAllStudents:
    def __init__(self):
        pass

    def delete_all_students(self):
        confirm = messagebox.askyesno("Delete All Students", "Are you sure you want to delete all students?")
        if confirm:
            self.remove_all_students_from_csv()
            messagebox.showinfo("Success", "All students have been deleted.")

    def remove_all_students_from_csv(self):
        with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Date of Birth', 'Student Code', 'Class Code', 'ECTs', 'Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header only (empty file)
