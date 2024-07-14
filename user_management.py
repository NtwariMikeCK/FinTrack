#!/usr/bin/python3
"""
user_management.py

A Python script to manage user details for the FinTrack app.

Modules:
    - os: For file handling.
    - tabulate: For displaying data in a table format.

Functions:
    add_user: Adds a new user to the user details file.
    view_users: Displays all user details from the file in a table format.
"""

import os
from tabulate import tabulate

USER_FILE = 'user_details.txt'

def add_user(name, email, financial_status, lifestyle):
    """Adds a new user to the user details file."""
    with open(USER_FILE, 'a') as file:
        file.write(f"{name},{email},{financial_status},{lifestyle}\n")
    print("User added successfully!")

def view_users():
    """Displays all user details from the user details file in a table format."""
    if not os.path.exists(USER_FILE):
        print("No users found.")
        return

    with open(USER_FILE, 'r') as file:
        users = file.readlines()
        if users:
            table_data = []
            for user in users:
                name, email, financial_status, lifestyle = user.strip().split(',')
                table_data.append([name, email, financial_status, lifestyle])
            
            headers = ["Name", "Email", "Financial Status", "Lifestyle"]
            print("\nUser Details:")
            print(tabulate(table_data, headers, tablefmt="grid"))
        else:
            print("No users found.")

def main():
    """Main function to manage user details."""
    while True:
        print("\nUser Management Menu")
        print("1. Add User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            financial_status = input("Enter financial status (rich/moderate/poor): ")
            lifestyle = input("Enter lifestyle preference (luxurious/cheap): ")
            add_user(name, email, financial_status, lifestyle)
        elif choice == '2':
            view_users()
        elif choice == '3':
            print("Exiting user management. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
