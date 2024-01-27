import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from database.models import Sklep, session

def delete_record(model_class, window_title, label_text):
    def submit_deletion():
        record_id = int(id_entry.get())
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            messagebox.showinfo("Success", f"Record ID {record_id} deleted successfully.")
        else:
            messagebox.showerror("Error", f"No record found with ID {record_id}.")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title(window_title)

    tk.Label(delete_window, text=label_text).pack()
    id_entry = tk.Entry(delete_window)
    id_entry.pack()
    submit_button = tk.Button(delete_window, text="Delete", command=submit_deletion)
    submit_button.pack()


def add_shop():
    def submit_shop():
        adres = adres_entry.get()
        nazwa_sieci = nazwa_sieci_entry.get()
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())

        new_shop = Sklep(adres=adres, nazwa_sieci=nazwa_sieci, latitude=latitude, longitude=longitude)

        session.add(new_shop)
        session.commit()

        add_shop_window.destroy()

    add_shop_window = tk.Toplevel()
    add_shop_window.title("Dodaj nową placówkę sklepu")

    tk.Label(add_shop_window, text="Adres:").grid(row=0, column=0)
    adres_entry = tk.Entry(add_shop_window)
    adres_entry.grid(row=0, column=1)

    tk.Label(add_shop_window, text="Nazwa Sieci:").grid(row=1, column=0)
    nazwa_sieci_entry = tk.Entry(add_shop_window)
    nazwa_sieci_entry.grid(row=1, column=1)

    tk.Label(add_shop_window, text="Szerokość geograficzna:").grid(row=2, column=0)
    latitude_entry = tk.Entry(add_shop_window)
    latitude_entry.grid(row=2, column=1)

    tk.Label(add_shop_window, text="Długość geograficzna:").grid(row=3, column=0)
    longitude_entry = tk.Entry(add_shop_window)
    longitude_entry.grid(row=3, column=1)

    submit_button = tk.Button(add_shop_window, text="Dodaj sklep", command=submit_shop)
    submit_button.grid(row=4, column=0, columnspan=2)
    
def edit_shop():
    def get_shop_id():
        def update_shop():
            try:
                shop_id = int(id_entry.get())
                shop = session.query(Sklep).filter_by(id=shop_id).first()
                if shop:
                    id_window.destroy()
                    show_edit_form(shop)
                else:
                    messagebox.showerror("Błąd!", "Nie znaleziono sklepu o podanym ID.")
            except ValueError:
                messagebox.showerror("Błąd!", "Wprowadź poprawne ID sklepu.")

        id_window = Toplevel()
        id_window.title("Wprowadź ID sklepu")

        tk.Label(id_window, text="ID Sklepu:").pack()
        id_entry = tk.Entry(id_window)
        id_entry.pack()

        submit_button = tk.Button(id_window, text="Edytuj", command=update_shop)
        submit_button.pack()

    def show_edit_form(shop):
        def save_changes():
            shop.adres = adres_entry.get()
            shop.nazwa_sieci = nazwa_sieci_entry.get()
            shop.latitude = float(latitude_entry.get())
            shop.longitude = float(longitude_entry.get())
            session.commit()
            edit_window.destroy()
            messagebox.showinfo("Brawo!", "Dane skelpu zaaktualizowane pomyślnie!")

        edit_window = Toplevel()
        edit_window.title("Edytuj dane sklepu.")

        tk.Label(edit_window, text="Adres:").grid(row=0, column=0)
        adres_entry = tk.Entry(edit_window)
        adres_entry.insert(0, shop.adres)
        adres_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Nazwa Sieci:").grid(row=1, column=0)
        nazwa_sieci_entry = tk.Entry(edit_window)
        nazwa_sieci_entry.insert(0, shop.nazwa_sieci)
        nazwa_sieci_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Szerokość geograficzna:").grid(row=2, column=0)
        latitude_entry = tk.Entry(edit_window)
        latitude_entry.insert(0, str(shop.latitude))
        latitude_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Długość geograficzna:").grid(row=3, column=0)
        longitude_entry = tk.Entry(edit_window)
        longitude_entry.insert(0, str(shop.longitude))
        longitude_entry.grid(row=3, column=1)

        save_button = tk.Button(edit_window, text="Edytuj", command=save_changes)
        save_button.grid(row=4, column=0, columnspan=2)

    get_shop_id()

def remove_shop():
    delete_record(Sklep, "Delete Shop", "Enter Shop ID:")

def show_shops():
    sklepy_records = session.query(Sklep).all()
    display_shops(sklepy_records)

def display_shops(records):
    top = Toplevel()
    top.title("List of Sklepy")

    tree = ttk.Treeview(top, columns=('ID', 'Adres', 'Nazwa Sieci'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Adres', text='Adres')
    tree.heading('Nazwa Sieci', text='Nazwa Sieci')
    tree.column('ID', anchor=tk.CENTER)
    tree.column('Adres', anchor=tk.CENTER)
    tree.column('Nazwa Sieci', anchor=tk.CENTER)
    for shop in records:
        tree.insert('', tk.END, values=(shop.id, shop.adres, shop.nazwa_sieci))
    tree.pack(fill=tk.BOTH, expand=True)