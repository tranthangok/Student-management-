import tkinter as tk
from signin import LoginScreen
from mainscreen import MainScreen

def main():
    root = tk.Tk()  
    def on_login_success():
        root.destroy()
        main_window = tk.Tk() 
        main_window.title("Main Screen")
        main_screen = MainScreen(main_window)
    login_screen = LoginScreen(root)

    root.mainloop()

if __name__ == "__main__":
    main()
