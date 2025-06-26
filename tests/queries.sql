CREATE TABLE personal_info(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE KEY,
)