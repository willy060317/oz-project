USE airbnb;
SET SQL_SAFE_UPDATES = 0;
-- CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),email VARCHAR(100),phone VARCHAR(20));
-- INSERT INTO customers (name, email, phone) VALUES('민', 'min@gmail.com','010-3434-3434');
-- SELECT * FROM customers;
-- CREATE TABLE product (carname INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),price VARCHAR(100));
-- INSERT INTO product (name, price) VALUES('k5',900);
-- UPDATE product SET price = 30 WHERE carname = LAST_INSERT_ID();
-- CREATE TABLE office (worker INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),price VARCHAR(100));
-- INSERT INTO office (name, price) VALUES('한남동',9000);
-- 업데이트가 안
-- UPDATE office SET price = 90 WHERE worker = LAST_INSERT_ID();

-- SELECT * FROM customers;
-- SELECT * FROM product WHERE price <=80;
-- 업데이트 부터
-- SELECT email, COUNT(*) AS customerCount FROM customers GROUP BY email;
-- SELECT name, AVG(price) AS averagePrice FROM product
-- UPDATE customers SET name = 'woojin' WHERE id = 12;
-- SELECT * FROM customers;
-- SELECT * FROM product;

-- UPDATE product SET price = 900000 WHERE carname = 1;
-- SELECT * FROM product;
-- UPDATE office SET name = '대천동' WHERE worker = 1;
-- SELECT * FROM office;
-- UPDATE product SET price = price * 1.1;
-- SELECT * FROM product;
-- UPDATE office SET name = 'korea' WHERE name = '대천동';
-- SELECT * FROM office;		
UPDATE customers SET name = '한지' WHERE id BETWEEN 1 AND 3;
SELECT * FROM customers;
DELETE FROM customers WHERE name = '만';
DELETE FROM office WHERE price <= 9090
