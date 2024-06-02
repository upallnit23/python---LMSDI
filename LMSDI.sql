
USE librarymgmtsystem_db;
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(id),
    publication_date DATE,
    book_id INT NOT NULL UNIQUE
);

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    user_id INT NOT NULL UNIQUE
);

CREATE TABLE authors (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE genres (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50)
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES books(id),
    borrow_date DATE NOT NULL,
    return_date DATE
);

SELECT * from books