CREATE DATABASE p51_test;

CREATE TABLE animals (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL CHECK (name != ''),
    date_of_birth DATE NOT NULL,
    escape_attempts INTEGER NOT NULL,
    neutered BOOLEAN NOT NULL,
    weight_kg DECIMAL(5, 2) NOT NULL,
);

ALTER TABLE animals
    ADD CONSTRAINT animals_name_check CHECK (name <> '');

DELETE FROM animals;

SELECT * FROM animals;

INSERT INTO animals (
    name,
    date_of_birth,
    escape_attempts,
    neutered,
    weight_kg
)
VALUES 
    ('Agumon', '2020-02-03', 0, true, 10.23),
    ('Gabumon', '2018-11-15', 2, true, 8.00),
    ('Pikachu', '2021-01-07', 1, false, 15.04),
    ('Devimon', '2017-05-12', 5, true, 11.00);

DELETE FROM animals WHERE name ILIKE '%трын%';

UPDATE animals
SET weight_kg = weight_kg + 1
WHERE neutered = true;

SELECT 
    (CASE WHEN (weight_kg > 12.5)
        THEN 'big'
        ELSE 'small'
    END) "size", 
    COUNT(weight_kg) count
FROM animals GROUP BY "size";  

