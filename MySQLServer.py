import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize the connection variable
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",       # Replace with your MySQL username
            password=""        # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Specifically catch mysql.connector.Error
        # Print error message if connection or creation fails
        print(f"Error: {e}")

    finally:
        # Close the database connection if it was successfully established
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
create_database()
