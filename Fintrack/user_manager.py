#!/usr/bin/python3
# src/user_manager.py
import sqlite3

DATABASE = 'src/expense_tracker.db'

def create_users_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE NOT NULL,
                            budget REAL NOT NULL,
                            time_period_days INTEGER NOT NULL
                        )''')
        conn.commit()

def add_user(username, budget, time_period_days):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, budget, time_period_days) VALUES (?, ?, ?)',
                       (username, budget, time_period_days))
        conn.commit()

def get_user(username):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cursor.fetchone()

def list_users():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM users')
        return [row[0] for row in cursor.fetchall()]

# Ensure the users table is created when the module is imported
create_users_table()

