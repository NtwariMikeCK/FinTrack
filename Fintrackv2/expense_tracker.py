#!/usr/bin/python3
from registration import create_connection


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


# def view_total_expenses(email, fullname):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE email = %s AND fullname = %s ' , (email, fullname))
#     return cursor.fetchone()


# def view_remaining_balance(email, fullname):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE email = %s AND fullname = %s ' , (email, fullname))
#     return cursor.fetchone()


# def view_spending_rate(email, fullname):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users WHERE email = %s AND fullname = %s ' , (email, fullname))
#     return cursor.fetchone()



class spending:
    def __init__(self, budget_id):
        # self.email = email
        self.budget_id = budget_id

    def total_expenses(self):
      conn = create_connection()
      cursor = conn.cursor()
      cursor.execute('SELECT SUM(price) FROM expenses WHERE budget_id = %s', (self.budget_id,))
      result = cursor.fetchone()
      if result[0] is None:
        return 0
      else:
        return result[0]

    def remaining_balance(self):
      conn = create_connection()
      cursor = conn.cursor()
      cursor.execute('SELECT b.budget - SUM(e.price) FROM budget AS b JOIN expenses AS e ON b.budget_id = e.budget_id WHERE b.budget = %s' , (self.budget_id,))
      result = cursor.fetchone()
      if result[0] is None:
        return 0
      else:
        return result[0]


    def time_spent(self):
      conn = create_connection()
      cursor = conn.cursor()
      cursor.execute('SELECT DATEDIFF(end_date, start_date) FROM budget WHERE budget_id = %s', (self.budget_id,))
      result = cursor.fetchone()
      if result[0] is None:
        return 0
      else:
        return result[0]

    def spending_rate(self):
      total = self.total_expenses()
      time = self.time_spent
      if total == None or time == None:
         return 0
      else:
         spending_rate = total /time
         return spending_rate


    def budget_warning(self):
       spend_rate = self.spending_rate()


    def spending_summary(self):
     print("This is the summary of your budget plan")
     print(f' Your total expense is {self.total_expenses}')

