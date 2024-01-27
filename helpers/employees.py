import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from database.models import Pracownik, session

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

def add_employee():
    def submit_employee():
        imie = imie_entry.get()
        nazwisko = nazwisko_entry.get()
        adres_zamieszkania = adres_zamieszkania_entry.get()
        adres_pracy = adres_pracy_entry.get()
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())

        new_employee = Pracownik(imie=imie, nazwisko=nazwisko, adres_zamieszkania=adres_zamieszkania, 
                                adres_pracy=adres_pracy, latitude=latitude, longitude=longitude)

        session.add(new_employee)
        session.commit()

        add_employee_window.destroy()

    add_employee_window = tk.Toplevel()
    add_employee_window.title("Add New Employee")

    tk.Label(add_employee_window, text="Imie:").grid(row=0, column=0)
    imie_entry = tk.Entry(add_employee_window)
    imie_entry.grid(row=0, column=1)

    tk.Label(add_employee_window, text="Nazwisko:").grid(row=1, column=0)
    nazwisko_entry = tk.Entry(add_employee_window)
    nazwisko_entry.grid(row=1, column=1)

    tk.Label(add_employee_window, text="Adres Zamieszkania:").grid(row=2, column=0)
    adres_zamieszkania_entry = tk.Entry(add_employee_window)
    adres_zamieszkania_entry.grid(row=2, column=1)

    tk.Label(add_employee_window, text="Adres Pracy:").grid(row=3, column=0)
    adres_pracy_entry = tk.Entry(add_employee_window)
    adres_pracy_entry.grid(row=3, column=1)

    tk.Label(add_employee_window, text="Latitude:").grid(row=5, column=0)
    latitude_entry = tk.Entry(add_employee_window)
    latitude_entry.grid(row=5, column=1)

    tk.Label(add_employee_window, text="Longitude:").grid(row=6, column=0)
    longitude_entry = tk.Entry(add_employee_window)
    longitude_entry.grid(row=6, column=1)

    submit_button = tk.Button(add_employee_window, text="Submit", command=submit_employee)
    submit_button.grid(row=7, column=0, columnspan=2)

def edit_employee():
    def get_employee_id():
        def update_employee():
            try:
                employee_id = int(id_entry.get())
                employee = session.query(Pracownik).filter_by(id=employee_id).first()
                if employee:
                    id_window.destroy()
                    show_edit_form(employee)
                else:
                    messagebox.showerror("Error", "Employee not found with the provided ID.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid ID.")

        id_window = Toplevel()
        id_window.title("Enter Employee ID")

        tk.Label(id_window, text="Employee ID:").pack()
        id_entry = tk.Entry(id_window)
        id_entry.pack()

        submit_button = tk.Button(id_window, text="Submit", command=update_employee)
        submit_button.pack()

    def show_edit_form(employee):
        def save_changes():
            employee.imie = imie_entry.get()
            employee.nazwisko = nazwisko_entry.get()
            employee.adres_zamieszkania = adres_zamieszkania_entry.get()
            employee.adres_pracy = adres_pracy_entry.get()
            employee.latitude = float(latitude_entry.get())
            employee.longitude = float(longitude_entry.get())
            session.commit()
            edit_window.destroy()
            messagebox.showinfo("Success", "Employee updated successfully.")

        edit_window = Toplevel()
        edit_window.title("Edit Employee")

        tk.Label(edit_window, text="Imię:").grid(row=0, column=0)
        imie_entry = tk.Entry(edit_window)
        imie_entry.insert(0, employee.imie)
        imie_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="Nazwisko:").grid(row=1, column=0)
        nazwisko_entry = tk.Entry(edit_window)
        nazwisko_entry.insert(0, employee.nazwisko)
        nazwisko_entry.grid(row=1, column=1)

        tk.Label(edit_window, text="Adres zamieszkania:").grid(row=2, column=0)
        adres_zamieszkania_entry = tk.Entry(edit_window)
        adres_zamieszkania_entry.insert(0, employee.adres_zamieszkania)
        adres_zamieszkania_entry.grid(row=2, column=1)

        tk.Label(edit_window, text="Adres pracy:").grid(row=3, column=0)
        adres_pracy_entry = tk.Entry(edit_window)
        adres_pracy_entry.insert(0, employee.adres_pracy)
        adres_pracy_entry.grid(row=3, column=1)

        tk.Label(edit_window, text="Szerokość geograficzna:").grid(row=4, column=0)
        latitude_entry = tk.Entry(edit_window)
        latitude_entry.insert(0, str(employee.latitude))
        latitude_entry.grid(row=4, column=1)

        tk.Label(edit_window, text="Długość geograficzna:").grid(row=5, column=0)
        longitude_entry = tk.Entry(edit_window)
        longitude_entry.insert(0, str(employee.longitude))
        longitude_entry.grid(row=5, column=1)

        save_button = tk.Button(edit_window, text="Save", command=save_changes)
        save_button.grid(row=6, column=0, columnspan=2)

    get_employee_id()

def remove_employee():
    delete_record(Pracownik, "Delete Employee", "Enter Employee ID:")

def show_employees():
    pracownicy_records = session.query(Pracownik).all()
    display_employees(pracownicy_records)

def display_employees(records):
    top = tk.Toplevel()
    top.title("List of Pracownicy")

    tree = ttk.Treeview(top, columns=('ID', 'Imie', 'Nazwisko', 'Adres Zamieszkania'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Imie', text='Imie')
    tree.heading('Nazwisko', text='Nazwisko')
    tree.heading('Adres Zamieszkania', text='Adres Zamieszkania')

    tree.column('ID', anchor=tk.CENTER)
    tree.column('Imie', anchor=tk.CENTER)
    tree.column('Nazwisko', anchor=tk.CENTER)
    tree.column('Adres Zamieszkania', anchor=tk.CENTER)

    for pracownik in records:
        tree.insert('', tk.END, values=(pracownik.id, pracownik.imie, pracownik.nazwisko, pracownik.adres_zamieszkania))

    tree.pack(fill=tk.BOTH, expand=True)