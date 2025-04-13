-- create

INSERT INTO Customers (customer_id, first_name, last_name) VALUES
(4, 'Mace', 'Windu');

INSERT INTO Products (product_id, name, category, price) VALUES
(4, 'zen pond', 'artisan keycap', 55.00);


-- read

-- retrieve last_name, first_name of the customer from transaction 2
SELECT last_name, first_name
FROM Customers c
JOIN Transactions t ON c.customer_id = t.customer_id
WHERE t.trans_id = 2;

-- retrieve the all product_id's purchased by customer 3
SELECT product_id
FROM Purchase_items pui
JOIN Transactions t ON pui.trans_id = t.trans_id
WHERE t.customer_id = 3;

-- update

UPDATE Customers
SET email = 'm.windu123@gmail.com'
WHERE customer_id = 4;

UPDATE Products
SET price = 110.00
WHERE product_id = 1;

-- delete

-- delete employee 3 (need to set transactions with employee to NULL before deleting employee)
UPDATE Transactions
SET employee_id = NULL
WHERE employee_id = 3;

DELETE FROM Employees
WHERE employee_id = 3;






