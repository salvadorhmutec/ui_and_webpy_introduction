CREATE DATABASE demo_bot;

USE demo_bot;

CREATE TABLE productos(
    id_producto int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    producto varchar(100) NOT NULL,
    existencias int NOT NULL,
    precio float NOT NULLdemo_bot
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO productos (producto, existencias, precio)
VALUES ('Mouse bluetooth',10,145.00),
('Laptop HP 15, HDD 1TB',5,9890.90),
('Monitor 23 pulgadas, HP',7,2500.00);

SHOW TABLES;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'bot'@'localhost' IDENTIFIED BY 'bot.2019';
GRANT ALL PRIVILEGES ON demo_bot.* TO 'bot'@'localhost';
FLUSH PRIVILEGES;
