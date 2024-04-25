import tkinter as tk
from tkinter import ttk
from showstudents import ShowStudent  

class SearchStudent:
    def __init__(self, master):
        self.master = master
        self.master.title("Search Student")

        self.frame = ttk.Frame(self.master, padding="10")
        self.frame.pack()

        ttk.Label(self.frame, text="Search by Name or Student Code:").grid(row=0, column=0, sticky="w", pady=10)
        self.search_entry = ttk.Entry(self.frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(self.frame, text="Search", command=self.search_students).grid(row=0, column=2, padx=10, pady=10)

        columns = ("Name", "Date of Birth", "Student Code", "Class Code", "ECTs", "Score")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def search_students(self):
        search_text = self.search_entry.get().strip().lower()  # Get search text and convert to lowercase
        show_student = ShowStudent(self.tree)
        show_student.refresh_student_list()  
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Retrieve all students' data
        students = show_student.get_students_data()

        for student in students:
            if self.matches_search_criteria(student, search_text):
                self.tree.insert('', 'end', values=(
                    student['Name'],
                    student['Date of Birth'],
                    student['Student Code'],
                    student['Class Code'],
                    student['ECTs'],
                    student['Score']
                ))

    def matches_search_criteria(self, student, search_text):
        name = student['Name'].lower()
        student_code = student['Student Code'].lower()

        return (search_text in name or
                search_text in student_code)

    def show(self):
        self.master.mainloop()
