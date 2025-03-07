CREATE DATABASE meu_sistema;


USE meu_sistema;



CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha_hash VARCHAR(64) NOT NULL
);
INSERT INTO usuarios (email, senha_hash) 
VALUES ('anuar', SHA2('123', 256));


select * from usuarios;
