import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from database.models import Dostawca, session

def delete_record(model_class, window_title, label_text):
    def submit_deletion():
        record_id = int(id_entry.get())
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            messagebox.showinfo("Brawo!", f"Dostawca o ID {record_id} został usunięty pomyślnie.")
        else:
            messagebox.showerror("Błąd!", f"Brak dostawcy o ID {record_id}.")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title(window_title)

    tk.Label(delete_window, text=label_text).pack()
    id_entry = tk.Entry(delete_window)
    id_entry.pack()
    submit_button = tk.Button(delete_window, text="Usuń", command=submit_deletion)
    submit_button.pack()

def add_supplier():
    def submit_supplier():
        nazwa_dostawcy = nazwa_dostawcy_entry.get()
        adres_dostawcy = adres_dostawcy_entry.get()
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())

        new_supplier = Dostawca(nazwa_dostawcy=nazwa_dostawcy, adres_dostawcy=adres_dostawcy, latitude=latitude, longitude=longitude)

        session.add(new_supplier)
        session.commit()

        add_supplier_window.destroy()

    add_supplier_window = tk.Toplevel()
    add_supplier_window.title("Dodaj nowego dostawcę")

    tk.Label(add_supplier_window, text="Nazwa Dostawcy:").grid(row=0, column=0)
    nazwa_dostawcy_entry = tk.Entry(add_supplier_window)
    nazwa_dostawcy_entry.grid(row=0, column=1)

    tk.Label(add_supplier_window, text="Adres Dostawcy:").grid(row=1, column=0)
    adres_dostawcy_entry = tk.Entry(add_supplier_window)
    adres_dostawcy_entry.grid(row=1, column=1)

    tk.Label(add_supplier_window, text="Szerokość geograficzna:").grid(row=2, column=0)
    latitude_entry = tk.Entry(add_supplier_window)
    latitude_entry.grid(row=2, column=1)

    tk.Label(add_supplier_window, text="Długość geograficzna:").grid(row=3, column=0)
    longitude_entry = tk.Entry(add_supplier_window)
    longitude_entry.grid(row=3, column=1)

    submit_button = tk.Button(add_supplier_window, text="Dodaj", command=submit_supplier)
    submit_button.grid(row=4, column=0, columnspan=2)

def edit_supplier():
    def get_supplier_id():
        def update_supplier():
            try:
                supplier_id = int(id_entry.get())
                supplier = session.query(Dostawca).filter_by(id=supplier_id).first()
                if supplier:
                    id_window.destroy()
                    show_edit_form(supplier)
                else:
                    messagebox.showerror("Błąd!", "Dostawca o podanym ID nie został znaleziony.")
            except ValueError:
                messagebox.showerror("Błąd!", "Wprowadź istniejące ID.")

        id_window = Toplevel()
        id_window.title("Wprowadź ID dostawcy")

        tk.Label(id_window, text="ID dostawcy:").pack()
        id_entry = tk.Entry(id_window)
        id_entry.pack()

        submit_button = tk.Button(id_window, text="Edytuj", command=update_supplier)
        submit_button.pack()

    def show_edit_form(supplier):
        def save_changes():
            supplier.nazwa_dostawcy = nazwa_dostawcy_entry.get()
            supplier.adres_dostawcy = adres_dostawcy_entry.get()
            supplier.latitude = float(latitude_entry.get())
            supplier.longitude = float(longitude_entry.get())
            session.commit()
            edit_window.destroy()
            messagebox.showinfo("Brawo!", "Dane dostawcy zostały edytowane pomyślnie.")

        edit_window = Toplevel()
        edit_window.title("Edytuj dane dostawcy")

        tk.Label(edit_window, text="Nazwa Dostawcy:").grid(row=0, column=0)
        nazwa_dostawcy_entry = tk.Entry(edit_window)
        nazwa_dostawcy_entry.insert(0, supplier.nazwa_dostawcy)
        nazwa_dostawcy_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Adres Dostawcy:").grid(row=1, column=0)
        adres_dostawcy_entry = tk.Entry(edit_window)
        adres_dostawcy_entry.insert(0, supplier.adres_dostawcy)
        adres_dostawcy_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Szerokość geograficzna:").grid(row=2, column=0)
        latitude_entry = tk.Entry(edit_window)
        latitude_entry.insert(0, str(supplier.latitude))
        latitude_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Długość geograficzna:").grid(row=3, column=0)
        longitude_entry = tk.Entry(edit_window)
        longitude_entry.insert(0, str(supplier.longitude))
        longitude_entry.grid(row=3, column=1)

        save_button = tk.Button(edit_window, text="Zapisz", command=save_changes)
        save_button.grid(row=4, column=0, columnspan=2)

    get_supplier_id()

def remove_supplier():
    delete_record(Dostawca, "Usuń dostawcę", "Wprowadź ID dostawcy:")

def show_suppliers():
    dostawcy_records = session.query(Dostawca).all()
    display_suppliers(dostawcy_records)

def display_suppliers(records):
    top = tk.Toplevel()
    top.title("Lista dostawców")

    tree = ttk.Treeview(top, columns=('ID', 'Nazwa Dostawcy', 'Adres Dostawcy'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Nazwa Dostawcy', text='Nazwa Dostawcy')
    tree.heading('Adres Dostawcy', text='Adres Dostawcy')

    tree.column('ID', anchor=tk.CENTER)
    tree.column('Nazwa Dostawcy', anchor=tk.CENTER)
    tree.column('Adres Dostawcy', anchor=tk.CENTER)

    for dostawca in records:
        tree.insert('', tk.END, values=(dostawca.id, dostawca.nazwa_dostawcy, dostawca.adres_dostawcy))

    tree.pack(fill=tk.BOTH, expand=True)