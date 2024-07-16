#!/usr/bin/python3
# src/expense_tracker.py

class ExpenseTracker:
    def __init__(self, budget, time_period_days):
        self.budget = budget
        self.time_period_days = time_period_days
        self.expenses = []

    def add_expense(self, amount, product, description):
        self.expenses.append({'amount': amount,'product': product , 'description': description})

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self):
        return self.budget - self.get_total_expenses()

    def get_spending_rate(self):
        days_passed = min(len(self.expenses), self.time_period_days)
        return self.get_total_expenses() / days_passed if days_passed > 0 else 0

    def check_budget_warning(self):
        if self.get_remaining_budget() <= (self.budget * 0.1):
            return "Warning: You are about to finish your budget!"
        return "You are within your budget."
    
    def spending_summary(self):
        return self.expenses
        #spending rate
        
        #list of expenses
        print(expense['product'] for expense in self.expenses)
        #warning
