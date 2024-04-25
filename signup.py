import tkinter as tk
from tkinter import ttk, messagebox
import csv

class SignupScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign up")

        self.frame = ttk.Frame(self.master, padding="30")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.label_username = ttk.Label(self.frame, text="Username:")
        self.label_password = ttk.Label(self.frame, text="Password:")
        self.entry_username = ttk.Entry(self.frame)
        self.entry_password = ttk.Entry(self.frame, show="*")  
        self.show_password_var = tk.BooleanVar(value=False)
        self.check_show_password = ttk.Checkbutton(self.frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.btn_signup = ttk.Button(self.frame, text="Sign up", command=self.signup)

        self.label_username.grid(row=0, column=0, sticky="w", pady=10)
        self.entry_username.grid(row=0, column=1, sticky="w", pady=10)
        self.label_password.grid(row=1, column=0, sticky="w", pady=10)
        self.entry_password.grid(row=1, column=1, sticky="w", pady=10)
        self.check_show_password.grid(row=2, columnspan=2, pady=10)
        self.btn_signup.grid(row=3, columnspan=2, pady=10)

    def signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra điều kiện để đăng ký tài khoản
        if self.is_valid_input(username, password):
            if not self.is_username_taken(username):
                self.save_account(username, password)
                messagebox.showinfo("Notification", "Your account has been successfully created!")
                self.master.destroy() 
            else:
                messagebox.showerror("Error", "The username is already taken. Please choose another one.")
        else:
            messagebox.showerror("Error", "Please fill in all the information.")

    def is_valid_input(self, username, password):
        return username.strip() != "" and password.strip() != ""

    def is_username_taken(self, username):
        with open('accounts.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Username'] == username:
                    return True
        return False
    def save_account(self, username, password):
        with open('accounts.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Username', 'Password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'Username': username, 'Password': password})

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.entry_password.config(show="")  
        else:
            self.entry_password.config(show="*")  

    def return_to_login_screen(self):
        self.master.destroy()
        from signin import LoginScreen 
        login_window = tk.Toplevel(self.master)
        LoginScreen(login_window)
