#!/usr/bin/python3
# src/recommender.py

class Recommender:
    def __init__(self):
        self.questions = [
            "What are your top three categories of spending each month?",
            "How do you typically decide where to shop for necessities like groceries, clothing, or household items?",
            "On average, how much do you spend on dining out or entertainment per month?",
            "How important are brand names and quality when you make purchases?",
            "Do you actively look for discounts, sales, or use coupons when shopping? If so, how often?"
        ]

    def ask_questions(self):
        responses = []
        for question in self.questions:
            response = input(question + " ")
            responses.append(response)
        return responses

    def recommend(self, responses):
        # Dummy logic for recommendations, you can enhance this with more complex logic
        if "discounts" in responses[-1].lower():
            return "We recommend you shop at discount stores like Walmart or use online coupon sites."
        elif "brand names" in responses[3].lower():
            return "We recommend you shop at high-end stores or specialty shops."
        else:
            return "We recommend you shop at mid-range stores like Target or local supermarkets."
