import tkinter as tk
from tkinter import ttk, messagebox
import csv

class EditStudent:
    def __init__(self, master, student_data, refresh_callback):
        self.master = master
        self.student_data = student_data
        self.refresh_callback = refresh_callback

        self.top = tk.Toplevel(self.master)
        self.top.title("Edit Student")

        self.frame = ttk.Frame(self.top, padding="10")
        self.frame.pack()

        # Create labels and entry widgets for editing student information
        self.entry_widgets = {}
        row = 0
        for key in self.student_data:
            ttk.Label(self.frame, text=key + ":").grid(row=row, column=0, sticky="w", pady=5)
            entry = ttk.Entry(self.frame, width=30)
            entry.grid(row=row, column=1, pady=5)
            entry.insert(0, str(self.student_data[key]))  
            self.entry_widgets[key] = entry
            row += 1

        ttk.Button(self.frame, text="Save Changes", command=self.save_changes).grid(row=row, columnspan=2, pady=20)

    def save_changes(self):
        updated_data = {}
        for key in self.entry_widgets:
            updated_data[key] = self.entry_widgets[key].get().strip()

        result = self.update_student_data(updated_data)

        if result == "Student updated successfully.":
            messagebox.showinfo("Success", "Student updated successfully.")
            self.refresh_callback()  
            self.top.destroy() 
        else:
            messagebox.showerror("Error", result)

    def update_student_data(self, updated_data):
        if not all(updated_data.values()):
            return "Please fill in all fields."

        try:
            ects = int(updated_data['ECTs'])
            score = float(updated_data['Score'])
        except ValueError:
            return "ECTs must be an integer between 0 and 240. Score must be a float between 0 and 5."

        if not (0 <= ects <= 240):
            return "ECTs must be between 0 and 240."

        if not (0 <= score <= 5):
            return "Score must be between 0 and 5."

        students = []
        with open('students.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Student Code'] == self.student_data['Student Code']:
                    row.update(updated_data)
                students.append(row)

        with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'Date of Birth', 'Student Code', 'Class Code', 'ECTs', 'Score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

        return "Student updated successfully."
