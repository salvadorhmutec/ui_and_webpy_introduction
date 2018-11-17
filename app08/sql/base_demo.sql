CREATE DATABASE base_demo;

USE base_demo;

CREATE TABLE datos(
    email varchar(50) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO datos (email, password)
VALUES ('dejah@email','1234'),('jhon@email','5678');

SHOW TABLES;

SELECT * FROM datos;

DESCRIBE datos;

SELECT "Creando un usuario y asignandolo a la base de datos" as "Mensaje";
-- CREATE USER 'kuorra'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON base_demo.* TO 'kuorra'@'localhost';
-- GRANT ALL PRIVILEGES ON base_demo.* TO kuorra@'%' IDENTIFIED BY 'kuorra.remote';

FLUSH PRIVILEGES;
