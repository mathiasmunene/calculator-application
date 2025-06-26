CREATE TABLE personal_info(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

INSERT INTO personal_info (first_name, last_name, middle_name, age, email)
VALUES ('John', 'Doe', 'Michael', 30, 'john.doe@example.com'),
       ('Jane', 'Smith', 'Ann', 25, 'jane.smith@example.com'),
       ('Emily', 'Davis', NULL, 22, 'emily.davis@example.com'); 

SELECT * FROM personal_info;