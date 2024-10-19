import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='@Mazabuka100'  
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Creating the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
