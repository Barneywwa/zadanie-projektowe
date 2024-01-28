import tkinter as tk
from tkinter import messagebox
from database.models import Pracownik, Dostawca, Dostawa, session
from helpers.employees import display_employees
from helpers.suppliers import display_suppliers

def show_employees_of_facility():
    ask_for_address_and_display(show_employees_of_specific_facility)

def show_suppliers_of_facility():
    ask_for_address_and_display(show_suppliers_of_specific_facility)

def ask_for_address_and_display(display_function):
    def submit_address():
        address = address_entry.get()
        display_function(address)
        address_window.destroy()

    address_window = tk.Toplevel()
    address_window.title("Wprowadź adres sklepu")

    tk.Label(address_window, text="Adres sklepu:").pack()
    address_entry = tk.Entry(address_window)
    address_entry.pack()
    submit_button = tk.Button(address_window, text="Wyświetl", command=submit_address)
    submit_button.pack()

def show_employees_of_specific_facility(address):
    employees = session.query(Pracownik).filter(Pracownik.adres_pracy == address).all()
    display_employees(employees)

def show_suppliers_of_specific_facility(address):
    suppliers = session.query(Dostawca).join(Dostawa, Dostawca.nazwa_dostawcy == Dostawa.nazwa_dostawcy).filter(Dostawa.adres_dostawy == address).all()
    display_suppliers(suppliers)
    
def delete_record(model_class, window_title, label_text):
    def submit_deletion():
        record_id = int(id_entry.get())
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            messagebox.showinfo("Brawo!", f"Rekord o ID {record_id} został usunięty pomyślnie.")
        else:
            messagebox.showerror("Błąd!", f"Nie znaleziono rekordu o ID {record_id}.")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title(window_title)

    tk.Label(delete_window, text=label_text).pack()
    id_entry = tk.Entry(delete_window)
    id_entry.pack()
    submit_button = tk.Button(delete_window, text="Usuń", command=submit_deletion)
    submit_button.pack()