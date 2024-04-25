import tkinter as tk
from tkinter import ttk, messagebox
import csv

class AddStudent:
    def __init__(self, master, refresh_callback):
        self.master = master
        self.refresh_callback = refresh_callback

        self.top = tk.Toplevel(self.master)
        self.top.title("Add Student")

        self.frame = ttk.Frame(self.top, padding="5")
        self.frame.pack()

        ttk.Label(self.frame, text="Name:").grid(row=0, column=0, sticky="w", pady=10)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, pady=10)

        ttk.Label(self.frame, text="Date of Birth (DD-MM-YYYY):").grid(row=1, column=0, sticky="w", pady=10)
        self.dob_entry = ttk.Entry(self.frame)
        self.dob_entry.grid(row=1, column=1, pady=10)

        ttk.Label(self.frame, text="Student Code:").grid(row=2, column=0, sticky="w", pady=10)
        self.student_code_entry = ttk.Entry(self.frame)
        self.student_code_entry.grid(row=2, column=1, pady=10)

        ttk.Label(self.frame, text="Class Code:").grid(row=3, column=0, sticky="w", pady=10)
        self.class_code_entry = ttk.Entry(self.frame)
        self.class_code_entry.grid(row=3, column=1, pady=10)

        ttk.Label(self.frame, text="ECTs (0-240):").grid(row=4, column=0, sticky="w", pady=10)
        self.ects_entry = ttk.Entry(self.frame)
        self.ects_entry.grid(row=4, column=1, pady=10)

        ttk.Label(self.frame, text="Score (0-5):").grid(row=5, column=0, sticky="w", pady=10)
        self.score_entry = ttk.Entry(self.frame)
        self.score_entry.grid(row=5, column=1, pady=10)

        ttk.Button(self.frame, text="Add Student", command=self.handle_add_student).grid(row=6, columnspan=2, pady=20)

    def handle_add_student(self):
        name = self.name_entry.get().strip()
        dob = self.dob_entry.get().strip()
        student_code = self.student_code_entry.get().strip()
        class_code = self.class_code_entry.get().strip()
        ects = self.ects_entry.get().strip()
        score = self.score_entry.get().strip()

        result = self.add_student(name, dob, student_code, class_code, ects, score)

        if result == "Student added successfully.":
            messagebox.showinfo("Success", "Student added successfully.")
            self.refresh_callback() 
            self.clear_entries()  # Clear input fields
        else:
            messagebox.showerror("Error", result)

    def add_student(self, name, dob, student_code, class_code, ects, score):
        if not (name and dob and student_code and class_code and ects and score):
            return "Please fill in all fields."

        try:
            ects = int(ects)
            score = float(score)
        except ValueError:
            return "ECTs must be an integer between 0 and 240. Score must be a float between 0 and 5."

        if not (0 <= ects <= 240):
            return "ECTs must be between 0 and 240."

        if not (0 <= score <= 5):
            return "Score must be between 0 and 5."

        if self.is_student_code_taken(student_code):
            return "Student Code already exists. Please choose another one."

        with open('students.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Date of Birth', 'Student Code', 'Class Code', 'ECTs', 'Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'Name': name,
                'Date of Birth': dob,
                'Student Code': student_code,
                'Class Code': class_code,
                'ECTs': ects,
                'Score': score
            })

        return "Student added successfully."

    def is_student_code_taken(self, student_code):
        with open('students.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Student Code'] == student_code:
                    return True
        return False

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.student_code_entry.delete(0, tk.END)
        self.class_code_entry.delete(0, tk.END)
        self.ects_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)

    def show(self):
        self.master.wait_window(self.top)
