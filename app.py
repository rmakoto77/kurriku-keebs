import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root=tk.Tk()
root.title("Kurriku Keebs Admin")
root.geometry("1000x600")

tree=ttk.Treeview(root)
tree.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

root.mainloop()