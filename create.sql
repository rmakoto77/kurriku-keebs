CREATE TABLE Products (
	product_id INTEGER PRIMARY KEY AUTOINCREMENT,
	name,
	category,
	price

	-- functional dependency
	-- product_id -> name, category, price
);

CREATE TABLE Employees (
	employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name,
	last_name,
	position

	-- employee_id -> first_name, last_name, position
);

CREATE TABLE Customers (
	customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name,
	last_name,
	email

	-- customer_id -> first_name, last_name, email
);

CREATE TABLE Transactions (
	trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id,
	employee_id,
	trans_date DEFAULT CURRENT_TIMESTAMP,
	item_total,
	total_amount,
	
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
	FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)

	-- trans_id -> customer_id, employee_id, trans_date, item_total, total_amount
	-- FK customer_id creates relationship with Customers table
	-- FK employee_id creates relationship with Employees table
);

CREATE TABLE purchase_items (
	p_i_id INTEGER PRIMARY KEY AUTOINCREMENT,
	trans_id,
	product_id,
	
	FOREIGN KEY (trans_id) REFERENCES Transactions(trans_id),
	FOREIGN KEY (product_id) REFERENCES Products (product_id)

	-- trans_prod_id -> trans_id, product_id
	-- FK trans_id creates relationship with Transactions table
	-- FK product_id creates relationship with Products table
);