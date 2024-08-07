#!/usr/bin/python3
from tabulate import tabulate
import mysql.connector
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'remote-user'
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
        return conn
        # if conn.is_connected():
        #     # print('Query Executed Successfully')
        # return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


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



def check():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT email, fullname FROM users')
    return [row[0] for row in cursor.fetchall()]

def list_users():
    conn = create_connection()
    cursor = conn.cursor()
    query = '''
    SELECT email, fullname, age, livingplace
    FROM users  
    '''

    cursor.execute(query)
    result = cursor.fetchall()
    headers = ["Email", "Full name", "Age", "Living place"]
    table = tabulate(result, headers, tablefmt="pretty")
    print(table)
