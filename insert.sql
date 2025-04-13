INSERT INTO Products (product_id, name, category, price) VALUES
(1, 'Ducky One2Mini', 'keyboard', 99.00),
(2, 'gateron yellow', 'switch', 0.25),
(3, 'Mode Lotus', 'keycap set', 59.99);

INSERT INTO Employees (employee_id, first_name, last_name, position) VALUES
(1, 'Ben', 'Kenobi', 'Manager'),
(2, 'Leia', 'Organa', 'Team member'),
(3, 'Luke', 'Skywalker', 'Team member');

INSERT INTO Customers (customer_id, first_name, last_name, email) VALUES
(1, 'Lando', 'Calrissian', 'lcal789@gmail.com'),
(2, 'Boba', 'Fett', 'boba.fett2@icloud.com'),
(3, 'Rush', 'Clovis', 'r.clovis09@outlook.com');

INSERT INTO Transactions (trans_id, customer_id, employee_id, item_total, total_amount) VALUES
(1, 3, 1, 1, 99.00),
(2, 2, 1, 100, 25.00),
(3, 1, 3, 2, 158.99);

INSERT INTO Purchase_items (p_i_id, trans_id, product_id, sale_price) VALUES
(1, 1, 1, 99.00),
(2, 2, 2, 0.25),
(3, 3, 1, 99.00),
(4, 3, 3, 59.99);