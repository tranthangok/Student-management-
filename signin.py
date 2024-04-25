import tkinter as tk
from tkinter import ttk, messagebox
import csv
from mainscreen import MainScreen
from signup import SignupScreen  # Import SignupScreen

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign in")

        self.frame = ttk.Frame(self.master, padding="30")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.label_username = ttk.Label(self.frame, text="Username:")
        self.label_password = ttk.Label(self.frame, text="Password:")
        self.entry_username = ttk.Entry(self.frame)
        self.entry_password = ttk.Entry(self.frame, show="*")  # Hiển thị dạng '*' mặc định
        self.show_password_var = tk.BooleanVar(value=False)
        self.check_show_password = ttk.Checkbutton(self.frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.btn_login = ttk.Button(self.frame, text="Sign in", command=self.login)
        self.btn_signup = ttk.Button(self.frame, text="Sign up", command=self.open_signup_window)

        self.label_username.grid(row=0, column=0, sticky="w", pady=10)
        self.entry_username.grid(row=0, column=1, sticky="w", pady=10)
        self.label_password.grid(row=1, column=0, sticky="w", pady=10)
        self.entry_password.grid(row=1, column=1, sticky="w", pady=10)
        self.check_show_password.grid(row=2, columnspan=2, pady=10)
        self.btn_login.grid(row=3, columnspan=2, pady=10)
        self.btn_signup.grid(row=4, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.authenticate(username, password):
            messagebox.showinfo("Notification", "Successfully signed in!")
            self.open_main_screen()
        else:
            messagebox.showerror("Error", "The username or password is incorrect!")

    def authenticate(self, username, password):
        with open('accounts.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    return True
        return False

    def open_main_screen(self):
        self.master.withdraw()  # Ẩn cửa sổ đăng nhập
        main_window = tk.Toplevel(self.master)
        main_screen = MainScreen(main_window)

    def open_signup_window(self):
        signup_window = tk.Toplevel(self.master)
        signup_screen = SignupScreen(signup_window)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.entry_password.config(show="")  # Hiển thị mật khẩu
        else:
            self.entry_password.config(show="*")  # Ẩn mật khẩu 