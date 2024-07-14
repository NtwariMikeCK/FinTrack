#!/usr/bin/python3
"""
3-fintrack.py

A Python script for providing recommendations based on user preferences and a small game to understand their financial status and lifestyle for the FinTrack app.

Modules:
    - requests: For making HTTP requests to get recommendations from websites.
    - tabulate: For displaying tabulated data.

Classes:
    - RecommendationSystem: Handles user inputs and provides personalized recommendations.
"""

import os
from tabulate import tabulate

class RecommendationSystem:
    """
    A class to handle user inputs and provide personalized recommendations based on their financial status and lifestyle.

    Methods:
        ask_questions: Asks user questions to determine their financial status and lifestyle.
        get_recommendations: Provides recommendations based on user preferences.
        display_menu: Displays the menu and handles user input for different operations.
    """

    def __init__(self):
        self.financial_status = None
        self.lifestyle = None

    def ask_questions(self):
        """Asks user questions to determine their financial status and lifestyle."""
        print("Let's play a small game to know you better.")

        # Questions to determine financial status
        income = float(input("What is your monthly income? "))
        savings = float(input("How much do you save monthly? "))
        spending = float(input("How much do you spend monthly? "))

        if income > 1000 and savings > 500:
            self.financial_status = "rich"
        elif income > 500 and savings > 200:
            self.financial_status = "moderate"
        else:
            self.financial_status = "poor"

        # Questions to determine lifestyle
        lifestyle_preference = input("Do you prefer luxurious goods or cheap things? (luxurious/cheap): ")
        self.lifestyle = "luxurious" if lifestyle_preference == "luxurious" else "cheap"

    def get_recommendations(self):
        """Provides recommendations based on user preferences."""
        print("Tell us more about you by answering the following questions:")
        product = input("What do you want to buy? ")
        location = input("Location to buy from: ")

        # Example recommendations based on financial status and lifestyle
        if self.financial_status == "rich" and self.lifestyle == "luxurious":
            print(f"Since you are {self.financial_status} and prefer {self.lifestyle} goods, here are some recommendations:")
            recommendations = [
                {"store": "Luxury Store A", "product": product, "price": 500},
                {"store": "Luxury Store B", "product": product, "price": 450},
            ]
        elif self.financial_status == "moderate":
            print(f"Since you are {self.financial_status}, here are some recommendations:")
            recommendations = [
                {"store": "Moderate Store A", "product": product, "price": 300},
                {"store": "Moderate Store B", "product": product, "price": 250},
            ]
        else:
            print(f"Since you are {self.financial_status} and prefer {self.lifestyle} things, here are some recommendations:")
            recommendations = [
                {"store": "Cheap Store A", "product": product, "price": 100},
                {"store": "Cheap Store B", "product": product, "price": 80},
            ]

        # Display recommendations
        headers = ["Store", "Product", "Price"]
        rows = [[r["store"], r["product"], r["price"]] for r in recommendations]
        print(tabulate(rows, headers, tablefmt="grid"))

    def display_menu(self):
        """Displays the menu and handles user input for different operations."""
        while True:
            menu = [
                ["1", "Play Game and Get Recommendations"],
                ["2", "Main Menu"],
                ["3", "Exit"]
            ]
            print("\nRecommendations Menu")
            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))

            choice = input("Enter your choice: ")

            if choice == '1':
                self.ask_questions()
                self.get_recommendations()
            elif choice == '2':
                os.system('python3 1-fintrack.py')
                break
            elif choice == '3':
                print("Exiting the recommendation system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

def main():
    """Main function to run the RecommendationSystem app."""
    recommender = RecommendationSystem()
    recommender.display_menu()

if __name__ == "__main__":
    main()
