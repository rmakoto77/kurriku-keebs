''' Features:
        - View, add, update, delete records (CRUD)
            - load_customers()
            - add_customer()
            - load_products()
            - add_product()
            - update_product() --> update products table
            - delete_product()   
'''

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

conn=sqlite3.connect("kurriku_keebs.db")
cursor=conn.cursor()

root=tk.Tk()
root.title("Kurriku Keebs Admin")
root.geometry("1000x600")

tree=ttk.Treeview(root)
tree.pack()

def clear_tree():
    for i in tree.get_children():
        tree.delete(i)
        
def load_customers():
    clear_tree()
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    tree["columns"] = ("ID", "First", "Last", "email")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    for r in rows:
        tree.insert("", tk.END, values=r)

def load_products():
    clear_tree()
    cursor.execute("SELECT * FROM Products")
    rows=cursor.fetchall()
    tree["columns"] = ("ID", "Name", "Category", "Price")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    for r in rows:
        tree.insert("", tk.END, values=r)

frame = tk.Frame(root)
frame.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Load Products", command=load_products).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Load Customers", command=load_customers).grid(row=1, column=0, padx=5)

root.mainloop()