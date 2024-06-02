#Gym Database Management with Python and SQL
#Adding to the Library Management System

from mysql_connect import connect_database

#Functions used to add books, users, authors, and genres of books to the database in mySQL
def add_book(title, author_id, genre_id, publication_date, book_id):
    query = "INSERT INTO books (title, author_id, genre_id, publication_date, book_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, author_id, genre_id, publication_date, book_id))

def add_user(name, user_id):
    query = "INSERT INTO users (name, user_id) VALUES (%s, %s)"
    cursor.execute(query, (name, user_id))

def add_author(name, biography):
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, biography))

def add_genre(name, description, category):
    query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, description, category))


conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #(title, author_id, genre_id, publication_date, book_id):
        add_book("The Morning Sun", 1101, 2101, "2000-12-25", 101)

        #(name, user_id):
        add_user("Cindy Moon", 401)

        #(name, biography):
        add_author("James Candies", "James Candies primarily writes family-oriented stories.  His first book published in 1997.")

        #(name, description, category):
        add_genre("James Candies", "Primarily writes fictional novels, correlating with traditional family drama.", "Fiction")

        conn.commit()
        print("Above functions performed to add either books, users, authors, or genres to the library.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()