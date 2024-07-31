#!/usr/bin/python3
"""
1-fintrack.py

A Python script for the FinTrack app that includes a menu for tracking expenses, getting recommendations, and exiting the app.

Modules:
    - os: For running other Python scripts.
    - sqlite3: For interacting with the SQLite database.
    - datetime: For handling date and time for expense tracking.

Classes:
    - FinTrackApp: Handles the menu operations and functionality for tracking expenses and providing recommendations.
"""

import os
import sqlite3
import datetime
from tabulate import tabulate

class FinTrackApp:
    """
    A class to handle the FinTrack app operations.

    Methods:
        init_db: Initializes the SQLite database and creates the expenses table if it does not exist.
        track_expense: Tracks an expense by storing it in the database.
        get_recommendations: Provides financial recommendations based on tracked expenses.
        view_expenses: Displays all tracked expenses.
        display_menu: Displays the menu and handles user input for different operations.
    """

    def __init__(self, db_name='fintrack.db'):
        """
        Initializes the FinTrackApp class with the specified database name.

        Parameters:
            db_name (str): The name of the SQLite database file. Default is 'fintrack.db'.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """Initializes the SQLite database and creates the expenses table if it does not exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def track_expense(self):
        """Tracks an expense by storing it in the database."""
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category of the expense: ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a description (optional): ")

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        ''', (date, category, amount, description))
        conn.commit()
        conn.close()

        print("Expense tracked successfully!")

    def get_recommendations(self):
        """Provides financial recommendations based  preferences or  on tracked expenses."""
        # Run the 3-fintrack.py script file
        os.system('python3 3-fintrack.py')

    def view_expenses(self):
        """Displays all tracked expenses."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()
        conn.close()

        if rows:
            print("\nTracked Expenses:")
            headers = ["ID", "Date", "Category", "Amount", "Description"]
            print(tabulate(rows, headers, tablefmt="grid"))
        else:
            print("No expenses tracked yet.")

    def display_menu(self):
        """Displays the menu and handles user input for different operations."""
        while True:
            menu = [
                ["1", "Track Expenses"],
                ["2", "Recommendations"],
                ["3", "View Expenses"],
                ["4", "Expense Tracker Options"],
                ["5", "Exit"]
            ]
            print("\nMenu for the FinTrack App")
            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("Enter your choice: ")

            if choice == '1':
                self.track_expense()
            elif choice == '2':
                self.get_recommendations()
            elif choice == '3':
                self.view_expenses()
            elif choice == '4':
                # Run the 2-fintrack.py script
                os.system('python3 2-fintrack.py')
            elif choice == '5':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

def main():
    """Main function to run the FinTrack app."""
    app = FinTrackApp()
    app.display_menu()

if __name__ == "__main__":
    main()
