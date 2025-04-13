''' Features:
        - View, add, update, delete records (CRUD)
            - load_customers()
            - add_customer()
            - load_products()
            - add_product()
            - update_product() --> update products table
            - delete_product()
            
        - Buttons to run JOIN queries
            - join transactions and customers --> see how many transactions a customer has w us
            - join transactions, purchase_items, and customers --> pull previous products a customer bought  
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

def add_customer():
    try:
        cursor.execute("INSERT INTO Customers (first_name, last_name, email) VALUES (?, ?, ?)",
                        (entry_fname.get(), entry_lname.get(), entry_email.get()))
        conn.commit()
        load_customers()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_products():
    clear_tree()
    cursor.execute("SELECT * FROM Products")
    rows=cursor.fetchall()
    tree["columns"] = ("ID", "Name", "Category", "Price")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    for r in rows:
        tree.insert("", tk.END, values=r)

def add_product():
    try:
        name = entry_name.get()
        category = entry_cat.get()
        price = entry_price.get()
        cursor.execute("INSERT INTO Products (name, category, price) VALUES (?, ?, ?)",
                        (name, category, float(price),))
        conn.commit()
        load_products()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_product():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("No selection")
        return
    values = tree.item(selected, "values")
    print("values:", values)
    try:
        product_id = int(values[0])
        name = entry_name.get()
        category = entry_cat.get()
        price = float(entry_price.get())
        print(f"updating to: {product_id}, {name}, {category}, {price}")

        cursor.execute("UPDATE Products SET name = ?, category = ?, price = ? WHERE product_id = ?",
                       (name, category, price, product_id))
        conn.commit()
        load_products()
        messagebox.showinfo("Success")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_product():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("No selection")
        return
    values = tree.item(selected, "values")
    try:
        product_id = values[0]
        cursor.execute("DELETE FROM Products WHERE product_id = ?", (int(product_id),))
        conn.commit()
        load_products()
        messagebox.showinfo("Success")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def customer_transactions(customer_id, treeview):
    if not customer_id.isdigit():
        messagebox.showerror("Invalid input")
        return
    customer_id = int(customer_id)
     
    try:
        cursor.execute("""
            SELECT t.trans_id, t.trans_date, t.item_total, t.total_amount,
                    GROUP_CONCAT(pi.product_id, ', ') AS product_ids
            FROM transactions t
            LEFT JOIN purchase_items pi ON t.trans_id = pi.trans_id
            WHERE t.customer_id = ?
            ORDER BY t.trans_date DESC
        """, (customer_id,))
        rows = cursor.fetchall()
        treeview.delete(*treeview.get_children())
        tree["columns"] = ("Transaction ID", "Date", "Item Total", "Total Amount", "Product IDs")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        if not rows:
            messagebox.showinfo("No Transactions", f"None found for customer ID {customer_id}")
        for r in rows:
            treeview.insert("", tk.END, values=r)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch transactions:str{e}")

def products_purchased(customer_id, treeview):
    if not customer_id.isdigit():
        messagebox.showerror("Invalid input")
        return
    customer_id = int(customer_id)
    
    try:
        cursor.execute("""
            SELECT p.name AS product_name,
            p.category,
            pi.sale_price,
            t.trans_date
            FROM transactions t
            JOIN purchase_items pi ON t.trans_id = pi.trans_id
            JOIN products p ON pi.product_id = p.product_id
            WHERE t.customer_id = ?
            ORDER BY t.trans_date DESC
        """, (customer_id,))
        rows = cursor.fetchall()
        treeview.delete(*treeview.get_children())
        tree["columns"] = ("Product Name", "Category", "Sale Price", "Date Purchased")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        if not rows:
            messagebox.showinfo("No Products", f"None found for customer ID {customer_id}")
        for r in rows:
            treeview.insert("", tk.END, values=r)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch products:str{e}")

def high_spenders():
    clear_tree()
    cursor.execute("""
                   SELECT first_name, last_name, email FROM customers
                   WHERE customer_id IN (
                        SELECT customer_id FROM transactions
                        GROUP BY customer_id
                        HAVING SUM(total_amount) > 50)
                   """)
    rows = cursor.fetchall()
    tree["columns"] = ("First", "Last", "Email")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    for r in rows:
        tree.insert("", tk.END, values=r)
    
# input fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=0, column=2)
entry_cat = tk.Entry(frame)
entry_cat.grid(row=0, column=3)

tk.Label(frame, text="Price").grid(row=0, column=4)
entry_price = tk.Entry(frame)
entry_price.grid(row=0, column=5)

tk.Label(frame, text="First Name").grid(row=1, column=0)
entry_fname = tk.Entry(frame)
entry_fname.grid(row=1, column=1)

tk.Label(frame, text="Last Name").grid(row=1, column=2)
entry_lname = tk.Entry(frame)
entry_lname.grid(row=1, column=3)

tk.Label(frame, text="Email").grid(row=1, column=4)
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=5)

tk.Label(frame, text="Customer ID").grid(row=2, column=0)
entry_customer_id = tk.Entry(frame)
entry_customer_id.grid(row=2, column=1)

# buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Load Products", command=load_products).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Add Product", command=add_product).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Update Product", command=update_product).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Delete Product", command=delete_product).grid(row=0, column=3, padx=5)

tk.Button(btn_frame, text="Load Customers", command=load_customers).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="Add Customer", command=add_customer).grid(row=1, column=1, padx=5)

# SQL buttons
query_frame = tk.Frame(root)
query_frame.pack(pady=10)

tk.Button(query_frame, text="Customer's Transactions", command=lambda: customer_transactions(entry_customer_id.get(), tree)).grid(row=0, column=0, padx=5)
tk.Button(query_frame, text="Products Purchased", command=lambda: products_purchased(entry_customer_id.get(), tree)).grid(row=0, column=1, padx=5)
tk.Button(query_frame, text="High Spenders", command=high_spenders).grid(row=0, column=2, padx=5)

root.mainloop()