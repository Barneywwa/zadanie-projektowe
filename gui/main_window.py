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
        
    def edit_shop(): pass
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
    
    def edit_employee(): pass
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
    
    def edit_supplier(): pass
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

    map_frame = tk.Frame(root)
    map_frame.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=10, pady=5)

    map_widget = TkinterMapView(map_frame, width=100, height=100, corner_radius=0)
    map_widget.pack(fill="both", expand=True)
    map_widget.set_position(52.237049, 21.017532)
    map_widget.set_zoom(10)

    root.mainloop()
