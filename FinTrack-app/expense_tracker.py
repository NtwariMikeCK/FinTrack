#!/usr/bin/python3
from tabulate import tabulate
from registration import create_connection
from datetime import datetime
from decimal import Decimal

def create_budget_plan(budget_id, email, budget, start_date, end_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budget (budget_id, email, budget, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s)
    ''', (budget_id, email, budget, start_date, end_date))
    conn.commit()
    print("budget plan successfully started.")

def add_expenses(expense_id, budget_id, product, description, price, purchase_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (expense_id, budget_id, product, description, price, purchase_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (expense_id, budget_id, product, description, price, purchase_date))
    conn.commit()
    print("Expense added successfully.")



class spending:
    def __init__(self, budget_id):
        # self.email = email
        self.budget_id = budget_id
    
    def total_expenses(self):
      conn = create_connection()
      cursor = conn.cursor()
      query = '''
      SELECT b.budget_id, b.budget, IFNULL(SUM(e.price), 0) AS total_expenses  
      FROM budget AS b 
      LEFT JOIN expenses AS e 
      ON b.budget_id = e.budget_id
      WHERE b.budget_id = %s 
      GROUP BY b.budget_id
      '''

      cursor.execute(query, (self.budget_id,))
      result = cursor.fetchall()
      headers = ["Budget ID", "Budget", "Total Expenses"]
      table = tabulate(result, headers, tablefmt="pretty")
      print(table)
    

    def remaining_balance(self):
      conn = create_connection()
      cursor = conn.cursor()
      query = '''
      SELECT b.budget_id, b.budget, IFNULL(SUM(e.price), 0) AS total_expenses, 
            (b.budget - IFNULL(SUM(e.price), 0)) AS remaining_balance 
      FROM budget AS b 
      LEFT JOIN expenses AS e 
      ON b.budget_id = e.budget_id
      WHERE b.budget_id = %s 
      GROUP BY b.budget_id
      '''

      cursor.execute(query, (self.budget_id,))
      result = cursor.fetchall()
      headers = ["Budget ID", "Budget", "Total Expenses", "Remaining Balance"]
      table = tabulate(result, headers, tablefmt="pretty")
      print(table)

    def total_expenses1(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(price) FROM expenses WHERE budget_id = %s', (self.budget_id,))
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def time_spent1(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT DATEDIFF(end_date, start_date) FROM budget WHERE budget_id = %s', (self.budget_id,))
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0
    

    def time_spent2(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT start_date FROM budget WHERE budget_id = %s', (self.budget_id,))
        start_date_result = cursor.fetchone()
        conn.close()
        
        if start_date_result is None or start_date_result[0] is None:
            return 0
        
        start_date = start_date_result[0]
        current_date = datetime.now().date()
        time_diff = (current_date - start_date).days
        return time_diff if time_diff > 0 else 1  # To avoid division by zero


    def actual_spending_rate(self):
        total = self.total_expenses1()
        time = self.time_spent1()
        if total == 0 or time == 0:
            return 0
        else:
            spending_rate = total / time
            return spending_rate
        
    def current_spending_rate(self):
        total = self.total_expenses1()
        time = self.time_spent2()
        if total == 0 or time == 0:
            return 0
        else:
            spending_rate = total / time
            return spending_rate
        
    def overall_spending(self):
        actual = self.actual_spending_rate()
        current = self.current_spending_rate()

         # Assuming `current` and `actual` are obtained from somewhere
        current = Decimal(self.current_spending_rate())  # Replace with actual value retrieval
        actual = Decimal(self.actual_spending_rate())   # Replace with actual value retrieval
        
        # Convert Decimal to float
        current = float(current)
        actual = float(actual)
        
        # Create the data in the expected format
        data = [
            ["Current Budget", current],
            ["Actual Spending", actual]
        ]
        
        headers = ["Description", "Amount"]
        table = tabulate(data, headers, tablefmt="pretty")
        print(table)

    def budget_warning(self):
        actual = self.actual_spending_rate()
        current = self.current_spending_rate()

         # Assuming `current` and `actual` are obtained from somewhere
        current = Decimal(self.current_spending_rate())  # Replace with actual value retrieval
        actual = Decimal(self.actual_spending_rate())   # Replace with actual value retrieval
        
        # Convert Decimal to float
        current = float(current)
        actual = float(actual)

        if current > actual:
            print("You are spending a lot each day than you should.")
            return "reduce"
        elif current < actual:
            print("You are spending less than you should, keep it up")
            return "increase"
        else:
            print("You are neither over-spending nor under-spending")
            return "maintain"
    
    
    def summary(self):
      conn = create_connection()
      cursor = conn.cursor()

      query = '''
      SELECT *
      FROM expenses 
      WHERE budget_id = %s
      '''

      cursor.execute(query, (self.budget_id,))
      result = cursor.fetchall()

      headers = ["Product", "Description", "Price", "Purchase_date"]
      table = tabulate(result, headers, tablefmt="pretty")
      print(table)
