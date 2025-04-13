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

frame = tk.Frame(root)
frame.pack(pady=10)

root.mainloop()