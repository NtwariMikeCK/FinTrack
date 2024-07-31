#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from registration import create_connection, register_user, list_users, check
from expense_tracker import spending, create_budget_plan, add_expenses
from datetime import datetime
from recommender import recommendation


def main():
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("Welcome to the Expense Tracker and Recommender App")
    print("We will help you to budget effectivelly bu tracking expenses for you")
    print("We will also recommend you places within your budget")

    while True:
        print("\nMenu:")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        print("1. Register User")
        print("2. Login User")
        print("3. List Users")
        print("4. Exit")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")

        choice = input("Choose an option: ")



        if choice == "1":
            email = input("Enter email: ")
            fullname = input("Enter username: ")
            age = int(input("Enter your age: "))
            livingplace = input("Enter where you stay: ")
            try:
                register_user(email, fullname, age, livingplace)
                print(f"User {fullname} registered successfully!")
                app_menu()
            except mysql.IntegrityError:
                print(f"Username {fullname} is already taken. Please choose a different username.")
        elif choice == "2":
            email = input("Enter email: ")
            fullname = input("Enter username: ")
            users = check()
            for user in users:
                if user in email:
                    print("Welcome back to FinTrack")
                    app_menu()
                # elif user not in email:
                #     print("User not found")
                else:
                    print("good")
        elif choice == "3":
            print("Registered Users:")
            list_users()
        elif choice == "4":
            print("Logging out...............")
            break
        else:
          print("Invalid choice. Please try again.")


def app_menu():
    while True:
        print("\nApp Menu:")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("1. Track Expenses")
        print("2. Recommendation")
        print("3. Logout")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")

        choice = input("Choose an option: ")

        if choice == "1":
            user_menu()
            
        elif choice == "2":
            recommend()
        elif choice == "3":
            print("Logging out.................")
            break
        else:
            print("Invalid choice. Please try again.")


def user_menu():
    while True:
        print("\nUser Menu:")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("1. start budget plan")
        print("2. Add Expense")
        print("3. View Total Expenses")
        print("4. View Remaining Budget")
        print("5. View Spending Rate")
        print("6. Check Budget Warning")
        print("7. Spending summary")
        print("8. Logout")
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")


        choice = input("Choose an option: ")

        if choice == "1":
            budget_id = int(input("Enter 1 if it is your first budget plan or 2 for so on: "))
            email = input("Enter your email: ")
            budget = int(input("Enter the amount for your budget plan: "))
            start_date_str = input("Enter the starting date of your budget plan, format yyyy-mm-dd: ")
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date_str = input("Enter the ending date of your budget plan, format yyyy-mm-dd: ")
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            create_budget_plan(budget_id, email, budget, start_date, end_date)

        elif choice == "2":
            expense_id = int(input("Enter the expense id: "))
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            product = input("Enter the name of the expense: ")
            description = input("Enter more information about the product: ")
            price = int(input("Enter the price of the product: "))
            purchase_date_str = input("When did you buy this product or service: ")
            purchase_date = datetime.strptime(purchase_date_str, '%Y-%m-%d').date()
            add_expenses(expense_id, budget_id, product, description, price, purchase_date)

        elif choice == "3":
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            total = spending(budget_id).total_expenses()
            print(f'This is your total expense {total}')
        elif choice == "4":
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            remaining = spending(budget_id).remaining_balance()
            print(f'This is your remaning balance {remaining}')
        elif choice == "5":
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            rate = spending(budget_id).overall_spending()
            print(f'This is your spending rate {spending(budget_id).current_spending_rate()}')
        elif choice == "6":
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            warning = spending(budget_id).budget_warning()
            print(f'Warning message: {warning}')
        elif choice == "7":
            budget_id = int(input("Which budget plan will this count for, enter budget_id: "))
            print(f'This is the summary of your spending for budget {budget_id}')
            summary = spending(budget_id).summary()
            print(summary)
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



# def recommend():
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
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
            
            elif question1 == "quality" and question2 == "no" and question3 == "no":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
            
            elif question1 == "quality" and question2 == "yes" and question3 == "no":
                spending_status = "Expensive"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
               
            elif question1 == "quality" and question2 == "no" and question3 == "yes":
                spending_status = "Cheap"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
               
            
            if question1 == "quantity" and question2 == "yes" and question3 == "yes":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
               
            elif question1 == "quantity" and question2 == "no" and question3 == "no":
                spending_status = "moderate"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
               
            elif question1 == "quantity" and question2 == "yes" and question3 == "no":
                spending_status = "Expensive"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
             
            elif question1 == "quantity" and question2 == "no" and question3 == "yes":
                spending_status = "Cheap"
                spending_categories = input("What do you want to buy 'clothes', 'groceries', 'dine out': ")
                result = recommendation(spending_status, spending_categories).retrieve_data()
                print(result)
        
        elif choice == "2":
            print("Logging out...")
            break  

if __name__ == "__main__":
    main()
