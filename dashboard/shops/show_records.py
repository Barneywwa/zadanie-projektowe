import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from database.config import database_url

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

def fetch_records():
    session = Session()
    sklepy_table = Table('sklepy', MetaData(), autoload_with=engine)
    records = session.query(sklepy_table).all()
    session.close()
    return records

def show_records(root):
    def update_treeview():
        records = fetch_records()
        for item in tree.get_children():
            tree.delete(item)
        for record in records:
            tree.insert('', tk.END, values=(record[0], record[1], record[2], record[3], record[4]))

    columns = ('column1', 'column2', 'column3', 'column4', 'column5')
    tree = ttk.Treeview(root, columns=columns, show='headings')

    tree.heading('column1', text='ID')
    tree.heading('column2', text='Adres sklepu')
    tree.heading('column3', text='Nazwa sieci')
    tree.heading('column4', text='Szerokość geograficzna')
    tree.heading('column5', text='Długość geograficzna')

    tree.grid(row=6, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

    button_submit = tk.Button(root, text="Wyświetl rekordy", command=update_treeview)
    button_submit.grid(row=5, column=0, columnspan=2)

    for col in columns:
        tree.column(col, width=150, anchor="center")