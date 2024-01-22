from decimal import Decimal
import tkinter as tk
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from database.config import database_url

global shop_name, shop_address, shop_latitude, shop_longitude

def add_record_form(root):
    global shop_name, shop_address, shop_latitude, shop_longitude

    shop_name = tk.Entry(root, width=25)
    shop_name.grid(row=0, column=1, padx=20)
    shop_address = tk.Entry(root, width=25)
    shop_address.grid(row=1, column=1, padx=20)
    shop_latitude = tk.Entry(root, width=25)
    shop_latitude.grid(row=2, column=1, padx=20)
    shop_longitude = tk.Entry(root, width=25)
    shop_longitude.grid(row=3, column=1, padx=20)

    shop_name_label = tk.Label(root, text="Nazwa sieci")
    shop_name_label.grid(row=0, column=0)
    shop_address_label = tk.Label(root, text="Adres sklepu")
    shop_address_label.grid(row=1, column=0)
    shop_latitude_label = tk.Label(root, text="Szerokość geograficzna")
    shop_latitude_label.grid(row=2, column=0)
    shop_longitude_label = tk.Label(root, text="Długość geograficzna")
    shop_longitude_label.grid(row=3, column=0)

    button_submit = tk.Button(root, text="Dodaj rekord", command=submit)
    button_submit.grid(row=4, column=1, columnspan=1, pady=5)

def submit():
    Session = sessionmaker(bind=engine)
    session = Session()

    latitude_value = shop_latitude.get()
    longitude_value = shop_longitude.get()
    new_record = shops_table.insert().values(
        adres=shop_address.get(),
        nazwa_sieci=shop_name.get(),
        latitude=latitude_value,
        longitude=longitude_value
    )

    session.execute(new_record)
    session.commit()
    session.close()

engine = create_engine(database_url)
metadata = MetaData()
shops_table = Table("sklepy", metadata, autoload_with=engine)