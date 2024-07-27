#!/usr/bin/python3

"""
o-fintrack.py

A Python script for user registration and login to a website using an SQLite database.
It handles user input, validates it, hashes passwords for security, and stores user information in the database.

Modules:
    - hashlib: For hashing passwords using SHA-256.
    - re: For validating email addresses with regex.
    - sqlite3: For interacting with the SQLite database.

Classes:
    - UserRegistration: Handles user registration and login logic, including database operations, password hashing, and email validation.
"""

import sqlite3
import hashlib
import re

class UserRegistration:
    """
    A class to handle user registration and login logic.

    Methods:
        init_db: Initializes the SQLite database and creates the users table if it does not exist.
        hash_password: Hashes a password using SHA-256.
        validate_email: Validates an email address using a regex pattern.
        register_user: Registers a new user with a username, email, and password.
        login_user: Logs in an existing user with a username and password.
    """

    def __init__(self, db_name='users.db'):
        """
        Initializes the UserRegistration class with the specified database name.

        Parameters:
            db_name (str): The name of the SQLite database file. Default is 'users.db'.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """Initializes the SQLite database and creates the users table if it does not exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def hash_password(self, password):
        """
        Hashes a password using SHA-256.

        Parameters:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_email(self, email):
        """
        Validates an email address using a regex pattern.

        Parameters:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def register_user(self, username, email, password):
        """
        Registers a new user with a username, email, and password.

        Parameters:
            username (str): The username of the new user.
            email (str): The email address of the new user.
            password (str): The password of the new user.

        Returns:
            bool: True if the registration was successful, False otherwise.
        """
        if not self.validate_email(email):
            print("Invalid email address.")
            return False

        hashed_password = self.hash_password(password)

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (username, email, hashed_password))
            conn.commit()
            print("User registered successfully!")
            return True
        except sqlite3.IntegrityError:
            print("Error: Username or email already exists.")
            return False
        finally:
            conn.close()

    def login_user(self, username, password):
        """
        Logs in an existing user with a username and password.

        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login was successful, False otherwise.
        """
        hashed_password = self.hash_password(password)

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE username=? AND password=?
        ''', (username, hashed_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

def main():
    """Main function to handle user input for registration or login."""
    user_registration = UserRegistration()

    print("Welcome to the User Registration and Login System")
    choice = input("Enter '1' to Register or '2' to Login: ")

    if choice == '1':
        username = input("Enter a username: ")
        email = input("Enter your email: ")
        password = input("Enter a password: ")

        if user_registration.register_user(username, email, password):
            print("Registration successful.")
        else:
            print("Registration failed.")
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if user_registration.login_user(username, password):
            print("Login successful.")
        else:
            print("Login failed.")
    else:
        print("Invalid choice. Please enter '1' to Register or '2' to Login.")

if __name__ == "__main__":
    main()
