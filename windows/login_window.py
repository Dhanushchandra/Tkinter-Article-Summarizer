import tkinter as tk
from tkinter import messagebox
from windows import main_window
from windows import signup_window

login_window = None  # Define login_window globally


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        login_window.destroy()
        main_window.show_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def goto_signup():
    login_window.destroy()
    signup_window.show_signup_window()


def run_login_window():
    global login_window  # Access the global login_window variable
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x150")

    # Username entry
    global username_entry
    username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 12))
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window, width=30, font=("Helvetica", 10))
    username_entry.pack(pady=5)

    # Password entry
    global password_entry
    password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 12))
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, width=30, show="*", font=("Helvetica", 10))
    password_entry.pack(pady=5)

    # Login button
    login_button = tk.Button(login_window, text="Login", command=login, bg="lightblue", font=("Helvetica", 12, "bold"))
    login_button.pack(pady=5)

    # Sign up button
    signup_button = tk.Button(login_window, text="Don't have an account? Sign up", command=goto_signup)
    signup_button.pack(pady=5)

    # Run the login window's main loop
    login_window.mainloop()


# Run the login window
# run_login_window()
