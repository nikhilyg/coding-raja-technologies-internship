import sqlite3  

class BudgetTracker:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(db_filename)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    amount REAL
                )
            ''')

    def add_income(self, amount):
        with self.conn:
            self.conn.execute('INSERT INTO income (amount) VALUES (?)', (amount,))

    def add_expense(self, category, amount):
        with self.conn:
            self.conn.execute('INSERT INTO expenses (category, amount) VALUES (?, ?)', (category, amount))

    def calculate_remaining_budget(self):
        with self.conn:
            total_income = self.conn.execute('SELECT COALESCE(SUM(amount), 0) FROM income').fetchone()[0]
            total_expenses = self.conn.execute('SELECT COALESCE(SUM(amount), 0) FROM expenses').fetchone()[0]
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def expense_analysis(self):
        with self.conn:
            expenses_by_category = self.conn.execute('''
                SELECT category, COALESCE(SUM(amount), 0) FROM expenses GROUP BY category
            ''').fetchall()
        return dict(expenses_by_category)

    def save_data(self):
        self.conn.commit()
        print("Data saved to SQLite database.")

    def load_data(self):
        print("Data loaded from SQLite database.")

def main():
    budget_tracker = BudgetTracker('budget_data.db')

    while True:
        print("\n=== Budget Tracker Menu ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Expense Analysis")
        print("5. Save Data")
        print("6. Load Data")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter income amount: $"))
                budget_tracker.add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "2":
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: $"))
                budget_tracker.add_expense(category, amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            remaining_budget = budget_tracker.calculate_remaining_budget()
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            expense_analysis = budget_tracker.expense_analysis()
            print("Expense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: ${amount}")
        elif choice == "5":
            budget_tracker.save_data()
        elif choice == "6":
            budget_tracker.load_data()
        elif choice == "0":
            budget_tracker.conn.close()
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
