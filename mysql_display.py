#Gym Database Management with Python and SQL
#Displaying Information in the Library Management System

from mysql_connect import connect_database

#Functions used to add books, users, authors, and genres of books to the database in mySQL
def display_books(title, author_id, genre_id, publication_date, book_id):
    query = "SELECT title, author_id, genre_id, publication_date, book_id FROM books VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, author_id, genre_id, publication_date, book_id))
    for books in cursor.fetchall():
        print(books)

def display_authors(name, biography):
    query = "SELECT name, biography FROM authors VALUES (%s, %s)"
    cursor.execute(query, (name, biography))
    for authors in cursor.fetchall():
        print(f"Author info: ")
        print(f"Name: {name}, Biography: {biography}")

def display_users(name, user_id):
    query = "SELECT name, user_id FROM users VALUES (%s, %s)"
    cursor.execute(query, (name, user_id))
    for users in cursor.fetchall():
        print(f"User info: ")
        print(f"Name: {name}, User Id: {user_id}")

def display_genres(cursor, keyword):
    query = "SELECT name, description, category FROM genres WHERE name LIKE %s"
    cursor.execute(query, ("%" + keyword + "%"))
    for genres in cursor.fetchall():
        print(cursor)


conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #(title, author_id, genre_id, publication_date, book_id):
        display_books(cursor)

        #(name, user_id):
        display_authors("Cindy Moon", 101)

        #(name, biography):
        display_authors("James Candies", "James Candies primarily writes family-oriented stories.  His first book published in 1997.")

        #(name, description, category):
        display_genres(cursor, "Comedy")

        conn.commit()
        print("Above functions performed to add either books, users, authors, or genres to the library.")

    except Exception as e:
        print(f"Error {e}")

    finally:
        cursor.close()
        conn.close()