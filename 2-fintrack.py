#!/usr/bin/python3
"""
2-fintrack.py

A Python script for tracking expenses, setting a project time period, and budget management for the FinTrack app.

Modules:
    - os: For running other Python scripts.
    - sqlite3: For interacting with the SQLite database.
    - datetime: For handling date and time for expense tracking.

Classes:
    - ExpenseTracker: Handles expense tracking, budget management, and spending summary.
"""

import os
import sqlite3
import datetime
from tabulate import tabulate

class ExpenseTracker:
    """
    A class to handle expense tracking, budget management, and spending summary.

    Methods:
        init_db: Initializes the SQLite database and creates the expenses table if it does not exist.
        set_project_period: Sets the project period by asking for a start and end date.
        set_budget: Sets the budget for the project period.
        track_expense: Tracks an expense by storing it in the database.
        spending_summary: Provides a summary of the spending within the project period.
        display_menu: Displays the menu and handles user input for different operations.
    """

    def __init__(self, db_name='fintrack.db'):
        """
        Initializes the ExpenseTracker class with the specified database name.

        Parameters:
            db_name (str): The name of the SQLite database file. Default is 'fintrack.db'.
        """
        self.db_name = db_name
        self.init_db()
        self.start_date = None
        self.end_date = None
        self.budget = None

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

    def set_project_period(self):
        """Sets the project period by asking for a start and end date."""
        self.start_date = input("Enter the project start date (YYYY-MM-DD): ")
        self.end_date = input("Enter the project end date (YYYY-MM-DD): ")
        print(f"Project period set from {self.start_date} to {self.end_date}.")

    def set_budget(self):
        """Sets the budget for the project period."""
        self.budget = float(input("Enter the budget for the project period: "))
        print(f"Budget set to {self.budget}.")

    def track_expense(self):
        """Tracks an expense by storing it in the database."""
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category of the expense: ")
        amount = float(input("Enter the amount: "))
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

    def spending_summary(self):
        """Provides a summary of the spending within the project period."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM expenses WHERE date BETWEEN ? AND ?
        ''', (self.start_date, self.end_date))
        rows = cursor.fetchall()
        conn.close()

        if rows:
            total_spent = sum(row[3] for row in rows)
            print("\nSpending Summary:")
            headers = ["ID", "Date", "Category", "Amount", "Description"]
            print(tabulate(rows, headers, tablefmt="grid"))
            print(f"\nTotal spent: {total_spent}")
            if self.budget:
                remaining_budget = self.budget - total_spent
                print(f"Remaining budget: {remaining_budget}")
        else:
            print("No expenses tracked yet for the specified period.")

    def display_menu(self):
        """Displays the menu and handles user input for different operations."""
        while True:
            menu = [
                ["1", "Set Project Period"],
                ["2", "Set Budget"],
                ["3", "Track Expense"],
                ["4", "Spending Summary"],
                ["5", "Main Menu"],
                ["6", "Exit"]
            ]
            print("\nExpense Tracking Menu")
            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("Enter your choice: ")

            if choice == '1':
                self.set_project_period()
            elif choice == '2':
                self.set_budget()
            elif choice == '3':
                self.track_expense()
            elif choice == '4':
                self.spending_summary()
            elif choice == '5':
                os.system('python3 1-fintrack.py')
                break
            elif choice == '6':
                print("Exiting the expense tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
