#mysql connection

import mysql.connector
from mysql.connector import Error

#Databse connection parameters used in other files to connect to database used in mySQL
def connect_database():
    db_name = "librarymgmtsystem_db"
    user = "root"
    password = "cooleyI1!"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connected in MySQL database successfully")
        
    except Error as e:
        print(f"Error: {e}")
    #Commented out finally section of program.  MySQL kept open to run other files using above login function.
    """finally:
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection is closed.")"""