#mysql connection

import mysql.connector
from mysql.connector import Error
from mysql_connect import connect_database

#Functions used to search for books in the database in mySQL
def search_btitle(cursor, keyword):
    query = "SELECT title, author_id, genre_id, publication_date, book_id FROM books WHERE title LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    print("Books with keyword in title: ")
    for books in cursor.fetchall():
        print(books)

def search_author(cursor, keyword):
    query = "SELECT author, biography FROM authors WHERE name LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    print(f"Authors with {keyword} in their names are: ")
    for authors in cursor.fetchall():
        print(authors)

def search_genres(cursor, keyword):
    query = "SELECT name, description, category FROM genres WHERE category LIKE %s"
    cursor.execute(query, ("%" + keyword + "%",))
    print(f"Authors from genres with category {keyword} are: ")
    for authors in cursor.fetchall():
        print(authors)

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        #Search query functions
        search_btitles(cursor, "Sun")

        search_authors(cursor, "Candy")

        search_genres(cursor, "romance")
        
        conn.commit()
        print("Above functions performed to add either books, users, authors, or genres to the library.")

    except Error as e:
        print(f"Error: {e}")
    #Commented out finally section of program.  MySQL kept open to run other files using above login function.
    finally:
        cursor.close()
        conn.close()