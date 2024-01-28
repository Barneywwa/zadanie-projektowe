import tkinter as tk
from tkinter import ttk, messagebox
from database.models import Dostawa, session

def delete_record(model_class, window_title, label_text):
    def submit_deletion():
        record_id = int(id_entry.get())
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            messagebox.showinfo("Brawo!", f"Dostawa o ID {record_id} został usunięty pomyślnie.")
        else:
            messagebox.showerror("Błąd!", f"Brak dostawy o ID {record_id}.")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title(window_title)

    tk.Label(delete_window, text=label_text).pack()
    id_entry = tk.Entry(delete_window)
    id_entry.pack()
    submit_button = tk.Button(delete_window, text="Usuń", command=submit_deletion)
    submit_button.pack()

def show_deliveries():
    dostawy_records = session.query(Dostawa).all()
    display_deliveries(dostawy_records)

def display_deliveries(records):
    top = tk.Toplevel()
    top.title("Lista dostaw")

    tree = ttk.Treeview(top, columns=('ID', 'Adres Dostawy', 'Nazwa Dostawcy'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Adres Dostawy', text='Adres Dostawy')
    tree.heading('Nazwa Dostawcy', text='Nazwa Dostawcy')

    tree.column('ID', anchor=tk.CENTER)
    tree.column('Adres Dostawy', anchor=tk.CENTER)
    tree.column('Nazwa Dostawcy', anchor=tk.CENTER)

    for dostawa in records:
        tree.insert('', tk.END, values=(dostawa.id, dostawa.adres_dostawy, dostawa.nazwa_dostawcy))

    tree.pack(fill=tk.BOTH, expand=True)

def add_delivery():
    def submit_delivery():
        adres_dostawy = adres_dostawy_entry.get()
        nazwa_dostawcy = nazwa_dostawcy_entry.get()

        new_delivery = Dostawa(adres_dostawy=adres_dostawy, nazwa_dostawcy=nazwa_dostawcy)

        session.add(new_delivery)
        session.commit()

        add_delivery_window.destroy()

    add_delivery_window = tk.Toplevel()
    add_delivery_window.title("Dodaj nową dostawę")

    tk.Label(add_delivery_window, text="Adres Dostawy:").grid(row=0, column=0)
    adres_dostawy_entry = tk.Entry(add_delivery_window)
    adres_dostawy_entry.grid(row=0, column=1)

    tk.Label(add_delivery_window, text="Nazwa Dostawcy:").grid(row=1, column=0)
    nazwa_dostawcy_entry = tk.Entry(add_delivery_window)
    nazwa_dostawcy_entry.grid(row=1, column=1)

    submit_button = tk.Button(add_delivery_window, text="Dodaj", command=submit_delivery)
    submit_button.grid(row=2, column=0, columnspan=2)

def delete_delivery():
    delete_record(Dostawa, "Usuń dostawę", "Podaj ID dostawy:")