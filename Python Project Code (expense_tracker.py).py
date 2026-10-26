import json
import os

FILENAME = "expenses.json"

def load_expenses():
    """Load expenses from a JSON file if it exists."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    """Save the current list of expenses to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense entry."""
    print("\n--- Add New Expense ---")
    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    
    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")
        return
        
    description = input("Enter description (optional): ").strip()

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    """Display all recorded expenses and total spending."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Expense List ---")
    print(f"{'Index':<6} | {'Category':<15} | {'Amount ($)':<12} | {'Description'}")
    print("-" * 60)
    
    total = 0
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx:<6} | {exp['category']:<15} | ${exp['amount']:<11.2f} | {exp['description']}")
        total += exp['amount']
    
    print("-" * 60)
    print(f"Total Spending: ${total:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses & Total")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select between 1 and 3.")

if __name__ == "__main__":
    main()