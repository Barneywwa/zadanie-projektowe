import tkinter as tk
from tkinter import ANCHOR, Toplevel, ttk, messagebox
from database.models import Sklep, Pracownik, Dostawca, Dostawa, session
from tkintermapview import TkinterMapView

#SKLEPY

def show_main_window():
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

#PRACOWNICY

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

#DOSTAWCY

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
        add_supplier_window.title("Add New Supplier")

        tk.Label(add_supplier_window, text="Nazwa Dostawcy:").grid(row=0, column=0)
        nazwa_dostawcy_entry = tk.Entry(add_supplier_window)
        nazwa_dostawcy_entry.grid(row=0, column=1)

        tk.Label(add_supplier_window, text="Adres Dostawcy:").grid(row=1, column=0)
        adres_dostawcy_entry = tk.Entry(add_supplier_window)
        adres_dostawcy_entry.grid(row=1, column=1)

        tk.Label(add_supplier_window, text="Latitude:").grid(row=2, column=0)
        latitude_entry = tk.Entry(add_supplier_window)
        latitude_entry.grid(row=2, column=1)

        tk.Label(add_supplier_window, text="Longitude:").grid(row=3, column=0)
        longitude_entry = tk.Entry(add_supplier_window)
        longitude_entry.grid(row=3, column=1)

        submit_button = tk.Button(add_supplier_window, text="Submit", command=submit_supplier)
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
                        messagebox.showerror("Error", "Supplier not found with the provided ID.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid ID.")

            id_window = Toplevel()
            id_window.title("Enter Supplier ID")

            tk.Label(id_window, text="Supplier ID:").pack()
            id_entry = tk.Entry(id_window)
            id_entry.pack()

            submit_button = tk.Button(id_window, text="Submit", command=update_supplier)
            submit_button.pack()

        def show_edit_form(supplier):
            def save_changes():
                supplier.nazwa_dostawcy = nazwa_dostawcy_entry.get()
                supplier.adres_dostawcy = adres_dostawcy_entry.get()
                supplier.latitude = float(latitude_entry.get())
                supplier.longitude = float(longitude_entry.get())
                session.commit()
                edit_window.destroy()
                messagebox.showinfo("Success", "Supplier updated successfully.")

            edit_window = Toplevel()
            edit_window.title("Edit Supplier")

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

            save_button = tk.Button(edit_window, text="Save", command=save_changes)
            save_button.grid(row=4, column=0, columnspan=2)

        get_supplier_id()
    
    def remove_supplier():
        delete_record(Dostawca, "Delete Supplier", "Enter Supplier ID:")
    def show_suppliers():
        dostawcy_records = session.query(Dostawca).all()
        display_suppliers(dostawcy_records)

    def display_suppliers(records):
        top = tk.Toplevel()
        top.title("List of Dostawcy")

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

#WSPÓLNE

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
        address_window.title("Enter Shop Address")

        tk.Label(address_window, text="Shop Address:").pack()
        address_entry = tk.Entry(address_window)
        address_entry.pack()
        submit_button = tk.Button(address_window, text="Submit", command=submit_address)
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

#DOSTAWY

    def show_deliveries():
        dostawy_records = session.query(Dostawa).all()
        display_deliveries(dostawy_records)

    def display_deliveries(records):
        top = tk.Toplevel()
        top.title("List of Deliveries")

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
        add_delivery_window.title("Add New Delivery")

        tk.Label(add_delivery_window, text="Adres Dostawy:").grid(row=0, column=0)
        adres_dostawy_entry = tk.Entry(add_delivery_window)
        adres_dostawy_entry.grid(row=0, column=1)

        tk.Label(add_delivery_window, text="Nazwa Dostawcy:").grid(row=1, column=0)
        nazwa_dostawcy_entry = tk.Entry(add_delivery_window)
        nazwa_dostawcy_entry.grid(row=1, column=1)

        submit_button = tk.Button(add_delivery_window, text="Submit", command=submit_delivery)
        submit_button.grid(row=2, column=0, columnspan=2)

    def delete_delivery():
        delete_record(Dostawa, "Delete Delivery", "Enter Delivery ID:")
    
#OKNO APLIKACJI

    root = tk.Tk()
    root.title("Zadanie projektowe BarneyWawa")
    root.geometry("1000x600")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)

    shop_frame = tk.LabelFrame(root, text="Sklepy")
    employee_frame = tk.LabelFrame(root, text="Pracownicy")
    supplier_frame = tk.LabelFrame(root, text="Dostawcy")
    employee_facility_frame = tk.LabelFrame(root, text="Pracownicy wybranej placówki")
    supplier_facility_frame = tk.LabelFrame(root, text="Dostawcy wybranej placówki")
    dostawa_frame = tk.LabelFrame(root, text="Dostawy")
    
    shop_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    employee_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    supplier_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    employee_facility_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    supplier_facility_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    dostawa_frame.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
    
    tk.Button(shop_frame, text="Dodaj", command=add_shop).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    tk.Button(shop_frame, text="Edytuj", command=edit_shop).grid(row=0, column=1, sticky="ew", padx=5, pady=2)
    tk.Button(shop_frame, text="Usuń", command=remove_shop).grid(row=0, column=2, sticky="ew", padx=5, pady=2)
    tk.Button(shop_frame, text="Wyświetl", command=show_shops).grid(row=0, column=3, sticky="ew", padx=5, pady=2)

    tk.Button(employee_frame, text="Dodaj", command=add_employee).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    tk.Button(employee_frame, text="Edytuj", command=edit_employee).grid(row=0, column=1, sticky="ew", padx=5, pady=2)
    tk.Button(employee_frame, text="Usuń", command=remove_employee).grid(row=0, column=2, sticky="ew", padx=5, pady=2)
    tk.Button(employee_frame, text="Wyświetl", command=show_employees).grid(row=0, column=3, sticky="ew", padx=5, pady=2)

    tk.Button(supplier_frame, text="Dodaj", command=add_supplier).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    tk.Button(supplier_frame, text="Edytuj", command=edit_supplier).grid(row=0, column=1, sticky="ew", padx=5, pady=2)
    tk.Button(supplier_frame, text="Usuń", command=remove_supplier).grid(row=0, column=2, sticky="ew", padx=5, pady=2)
    tk.Button(supplier_frame, text="Wyświetl", command=show_suppliers).grid(row=0, column=3, sticky="ew", padx=5, pady=2)

    tk.Button(employee_facility_frame, text="Wyświetl", command=show_employees_of_facility).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    tk.Button(supplier_facility_frame, text="Wyświetl", command=show_suppliers_of_facility).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    
    tk.Button(dostawa_frame, text="Wyświetl", command=show_deliveries).grid(row=0, column=0, sticky="ew", padx=5, pady=2)
    tk.Button(dostawa_frame, text="Dodaj", command=add_delivery).grid(row=0, column=1, sticky="ew", padx=5, pady=2)
    tk.Button(dostawa_frame, text="Usuń", command=delete_delivery).grid(row=0, column=2, sticky="ew", padx=5, pady=2)

    for frame in [shop_frame, employee_frame, supplier_frame]:
        for col in range(4):
            frame.grid_columnconfigure(col, weight=1)
    employee_facility_frame.grid_columnconfigure(0, weight=1)
    supplier_facility_frame.grid_columnconfigure(0, weight=1)
    dostawa_frame.grid_columnconfigure(0, weight=1)
    dostawa_frame.grid_columnconfigure(1, weight=1)
    dostawa_frame.grid_columnconfigure(2, weight=1)

    def update_map_with_markers(map_widget):
        map_widget.delete_all_marker()
        shops = session.query(Sklep).all()
        for shop in shops:
            map_widget.set_marker(shop.latitude, shop.longitude, text=f"Sklep: {shop.nazwa_sieci}", text_color="black", marker_color_circle="white", marker_color_outside="blue")
            
        employees = session.query(Pracownik).all()
        for employee in employees:
            map_widget.set_marker(employee.latitude, employee.longitude, text=f"Pracownik: {employee.imie} {employee.nazwisko}", text_color="black", marker_color_circle="white", marker_color_outside="yellow")

        suppliers = session.query(Dostawca).all()
        for supplier in suppliers:
            map_widget.set_marker(supplier.latitude, supplier.longitude, text=f"Dostawca: {supplier.nazwa_dostawcy}", text_color="black", marker_color_circle="white", marker_color_outside="green")

    def refresh_markers():
        update_map_with_markers(map_widget)

    map_frame = tk.Frame(root)
    map_frame.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=10, pady=5)

    map_widget = TkinterMapView(map_frame, width=100, height=100, corner_radius=0)
    map_widget.pack(fill="both", expand=True)
    map_widget.set_position(52.237049, 21.017532)
    map_widget.set_zoom(10)
    
    refresh_button = tk.Button(map_frame, text="Odśwież mapę", command=refresh_markers)
    refresh_button.pack(pady=10)
    
    update_map_with_markers(map_widget)

    root.mainloop()
