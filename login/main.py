import tkinter as tk
from tkinter import messagebox
from dashboard.main import initialize_dashboard

valid_username="123"
valid_password="123"

def check_login(username, password):
    if username == valid_username and password == valid_password:
        initialize_dashboard()
    else:
        messagebox.showerror("Błąd logowania", "Błędny login lub hasło. Spróbuj ponownie")

def submit_login():
    username = entry_username.get()
    password = entry_password.get()
    check_login(username, password)

root = tk.Tk()
root.title("Logowanie")

frame_login = tk.Frame(root)
frame_login.pack(padx=50, pady=30)

label_username = tk.Label(frame_login, text="Login:")
label_username.grid(row=0, column=0, sticky="e")
entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1)

label_password = tk.Label(frame_login, text="Hasło:")
label_password.grid(row=1, column=0, sticky="e", pady=10)
entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1)

button_submit = tk.Button(frame_login, text="Zaloguj", command=submit_login)
button_submit.grid(row=2, column=1, columnspan=2)

root.mainloop()