CREATE DATABASE webpy_mvc;

USE webpy_mvc;

CREATE TABLE personas(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    email varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO personas (nombre, email)
VALUES ('Dejah','dejah@barson'),
('Jhon','jhon@earth'),
('Carthoris','carthoris@barson');

SHOW TABLES;

SELECT * FROM personas;

DESCRIBE personas;

CREATE USER 'webpy'@'localhost' IDENTIFIED BY 'webpy.2019';
GRANT ALL PRIVILEGES ON webpy_mvc.* TO 'webpy'@'localhost';
FLUSH PRIVILEGES;
