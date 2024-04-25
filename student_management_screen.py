import tkinter as tk
from tkinter import ttk, messagebox
from addstudent import AddStudent
from showstudents import ShowStudent
from searchstudent import SearchStudent
from editstudent import EditStudent
from deletestudents import DeleteStudent, DeleteAllStudents

class StudentManageScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management")

        self.frame = ttk.Frame(self.master, padding="5")
        self.frame.pack()

        button_frame = ttk.Frame(self.frame)
        button_frame.pack(side=tk.TOP, pady=5)

        ttk.Button(button_frame, text="Add Student", command=self.open_add_student_window).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Show Students", command=self.refresh_student_list).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Search Students", command=self.open_search_student_window).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Edit Student", command=self.open_edit_student_window).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete Student", command=self.delete_selected_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete All Students", command=self.delete_all_students).pack(side=tk.LEFT, padx=5)

        # Create tree to display student list
        columns = ("Name", "Date of Birth", "Student Code", "Class Code", "ECTs", "Score")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=20)

        # Double-click binding to select and edit student
        self.tree.bind("<Double-1>", self.edit_selected_student)

    def open_add_student_window(self):
        add_student_window = AddStudent(self.master, self.refresh_student_list)
        add_student_window.show()

    def refresh_student_list(self):
        show_student = ShowStudent(self.tree)
        show_student.refresh_student_list()

    def open_search_student_window(self):
        search_window = tk.Toplevel(self.master)
        search_student = SearchStudent(search_window)
        search_student.show()

    def open_edit_student_window(self):
        selected_item = self.tree.focus()  
        if selected_item:
            student_data = self.tree.item(selected_item, 'values')
            edit_window = tk.Toplevel(self.master)
            EditStudent(edit_window, {
                "Name": student_data[0],
                "Date of Birth": student_data[1],
                "Student Code": student_data[2],
                "Class Code": student_data[3],
                "ECTs": student_data[4],
                "Score": student_data[5]
            }, self.refresh_student_list)
        else:
            messagebox.showwarning("Error", "Please select a student to edit.")

    def edit_selected_student(self, event):
        self.open_edit_student_window()

    def show(self):
        self.refresh_student_list()  
        self.master.mainloop()

    def delete_selected_student(self):
        delete_student = DeleteStudent(self.tree)
        delete_student.delete_selected_student()

    def delete_all_students(self):
        delete_all_students = DeleteAllStudents()
        delete_all_students.delete_all_students()
        self.refresh_student_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManageScreen(root)
    app.show()
