import tkinter as tk
from database.models import Sklep, Pracownik, Dostawca, session
from tkintermapview import TkinterMapView
from helpers.shops import add_shop, edit_shop, remove_shop, show_shops
from helpers.employees import add_employee, edit_employee, remove_employee, show_employees
from helpers.suppliers import add_supplier, edit_supplier, remove_supplier, show_suppliers
from helpers.deliveries import delete_delivery, show_deliveries, add_delivery
from helpers.specific_facility import show_employees_of_facility, show_suppliers_of_facility

def show_main_window():
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
    dostawa_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    employee_facility_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    supplier_facility_frame.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
    
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
