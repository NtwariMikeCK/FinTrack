#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate

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


class recommendation:
    def __init__(self, spending_status, spending_categories):
        self.spending_status = spending_status
        self.spending_categories = spending_categories

    def retrieve_data(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT spending_categories, spending_place, place_contacts FROM recommend WHERE spending_status = %s AND spending_categories = %s ' , (self.spending_status, self.spending_categories))
        result = cursor.fetchall()


        headers = ["categories", "Name", "Contacts"]
        table = tabulate(result, headers, tablefmt="pretty")
        print(table)




def recommend():
    while True:
        print("\nUser Menu:")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("1. Enter 1 to play a game to help us know about your spending habits")
        print("2. Logout")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")


        choice = input("Choose an option: ")

        if choice == "1":
            question1 = input("Do you prefer 'quality' or quantity': ")
            question2 = input("Do you care about brand names, 'yes' or 'no': ")
            question3 = input("Do you tend to bargain about price, 'yes' or 'no': ")
            question4 = input("Do you follow a budget plan, 'yes' or 'no': ")

            if question1 == "quality" and question2 == "yes" and question3 == "yes":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quality" and question2 == "no" and question3 == "no":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quality" and question2 == "yes" and question3 == "no":
                spending_status = "Expensive"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quality" and question2 == "no" and question3 == "yes":
                spending_status = "Cheap"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories


            if question1 == "quantity" and question2 == "yes" and question3 == "yes":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quantity" and question2 == "no" and question3 == "no":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quantity" and question2 == "yes" and question3 == "no":
                spending_status = "Expensive"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

            elif question1 == "quantity" and question2 == "no" and question3 == "yes":
                spending_status = "Cheap"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                return spending_status, spending_categories

        elif choice == "2":
            print("Logging out...")
            break
