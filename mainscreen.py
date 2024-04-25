import tkinter as tk
from tkinter import ttk, messagebox
import csv
from student_management_screen import StudentManageScreen

class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Screen")
        
        self.toolbar = ttk.Frame(self.master)
        self.toolbar.pack(side="top", fill="x")

        self.btn_create_file = ttk.Button(self.toolbar, text="Create Student File", command=self.create_student_file)
        self.btn_create_file.pack(side="left", padx=5)

        self.btn_logout = ttk.Button(self.toolbar, text="Log out", command=self.logout)
        self.btn_logout.pack(side="left", padx=5)

    def logout(self):
        self.master.destroy()  

    def create_student_file(self):
        student_file_window = tk.Toplevel(self.master)
        student_manage_screen = StudentManageScreen(student_file_window)
