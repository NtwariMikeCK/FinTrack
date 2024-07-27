#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'RutaGandA95'
DB_NAME = 'fintrack'

def create_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            print('Connected to MySQL database')
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# def create_users_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                email VARCHAR(255) AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                age FLOAT NOT NULL,
                livingplace VARCHAR(35)
            )
        ''')
        conn.commit()
        print("Table 'users' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


# def create_users_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(255) AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            age FLOAT NOT NULL,
            livingplace VARCHAR(35)
        )
    ''')
    conn.commit()
    print("Table 'users' created successfully.")

# def create_budget_table(conn):


    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(255) FOREIGN KEY,
            budget INT NOT NULL,
            start_date date NOT NULL,
            end_date date VARCHAR(35)
        )
    ''')
    conn.commit()
    print("Table 'users' created successfully.")


def register_user(email, fullname, age, livingplace):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (email, fullname, age, livingplace)
        VALUES (%s, %s, %s, %s)
    ''', (email, fullname, age, livingplace))
    conn.commit()
    print("User inserted successfully.")


def check_user(email, fullname):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s AND fullname = %s ' , (email, fullname))
    return cursor.fetchone()

def list_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchone()

def list_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT email, fullname FROM users')
    return [row[0] for row in cursor.fetchall()]



