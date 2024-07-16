#!/usr/bin/python3
# src/main.py

from expense_tracker import ExpenseTracker
from recommender import Recommender
from user_manager import add_user, get_user, list_users

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
            username = input("Enter username: ")
            age = input("Enter your age: ")
            livingplace = input("Enter where you stay: ")
            try:
                add_user(username, age, livingplace)
                print(f"User {username} registered successfully!")
                app_menu(tracker)
            except sqlite3.IntegrityError:
                print(f"Username {username} is already taken. Please choose a different username.")
        elif choice == "2":
            username = input("Enter username: ")
            user = get_user(username)
            if user:
                tracker = ExpenseTracker(user[2], user[3])  # budget and time_period_days are in 3rd and 4th columns
                app_menu(tracker)
            else:
                print("User not found. Please register first.")
        elif choice == "3":
            users = list_users()
            print("Registered Users:")
            for user in users:
                print(f"- {user}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def app_menu(tracker):
    while True:
        print("\nApp Menu:")
        print("1. Track Expenses")
        print("2. Recommendation")
        print("3. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            user_menu(tracker)
        elif choice == "2":
            recommender = Recommender()
            responses = recommender.ask_questions()
            recommendation = recommender.recommend(responses)
            print(recommendation)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(tracker):
    while True:
        print("\nUser Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Remaining Budget")
        print("4. View Spending Rate")
        print("5. Check Budget Warning")
        print("6. Spending summary")
        print("7. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            product = input("Enter product: ")
            description = input("Enter expense description: ")
            tracker.add_expense(amount, product, description)
        elif choice == "2":
            print(f"Total Expenses: {tracker.get_total_expenses()}")
        elif choice == "3":
            print(f"Remaining Budget: {tracker.get_remaining_budget()}")
        elif choice == "4":
            print(f"Spending Rate: {tracker.get_spending_rate()}")
        elif choice == "5":
            print(tracker.check_budget_warning())
        elif choice == "6":
            print(f"This is your summary for the expense tracker list: {tracker.spending_summary()}")
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
