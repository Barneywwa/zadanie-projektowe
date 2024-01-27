import tkinter as tk
from tkinter import messagebox
from .main_window import show_main_window

def authenticate(username, password):
    VALID_USERNAME = "123"
    VALID_PASSWORD = "123"
    return username == VALID_USERNAME and password == VALID_PASSWORD

def handle_submit(username_entry, password_entry, login_window):
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Błędne logowanie", "Hasło bądź login nieprawidłowe. Spróbuj ponownie.")

def show_login_form():
    login_window = tk.Tk()
    login_window.title("Logowanie")

    tk.Label(login_window, text="Login:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Hasło:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Zaloguj", command=lambda: handle_submit(username_entry, password_entry, login_window))
    login_button.grid(row=2, column=0, columnspan=2)

    login_window.mainloop()