import tkinter as tk
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from dashboard.shops.add_record_form import add_record_form
from dashboard.shops.show_records import show_records
from database.config import database_url

def initialize_dashboard():
    root = tk.Tk()
    root.title("Aplikacja")
    
    add_record_form(root=root)
    show_records(root=root)
    root.mainloop()