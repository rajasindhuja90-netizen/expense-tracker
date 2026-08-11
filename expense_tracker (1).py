"""
Expense Tracker
---------------
A simple command-line Python project to record, view, and analyze
your daily expenses. Data is saved to a CSV file so it persists
between runs.

Features:
- Add an expense (amount, category, description, date)
- View all expenses
- View total spending
- View spending by category
- Delete an expense by its ID
- Data is stored in expenses.csv (auto-created on first run)
"""

import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
FIELDS = ["id", "date", "category", "description", "amount"]


def init_file():
    """Create the CSV file with headers if it doesn't exist yet."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def get_next_id():
    """Work out the next available expense ID."""
    expenses = read_expenses()
    if not expenses:
        return 1
    return max(int(e["id"]) for e in expenses) + 1


def read_expenses():
    """Read all expenses from the CSV file into a list of dicts."""
    with open(FILENAME, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def add_expense():
    print("\n--- Add New Expense ---")
    category = input("Category (e.g. Food, Travel, Bills): ").strip().title()
    description = input("Description: ").strip()

    while True:
        amount_str = input("Amount (₹): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    date_str = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "id": get_next_id(),
        "date": date_str,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}",
    }

    with open(FILENAME, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(expense)

    print(f"Expense added successfully! (ID: {expense['id']})")


def view_expenses():
    expenses = read_expenses()
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 67)
    for e in expenses:
        print(f"{e['id']:<5}{e['date']:<12}{e['category']:<15}{e['description']:<25}{'₹' + e['amount']:>10}")


def view_total():
    expenses = read_expenses()
    total = sum(float(e["amount"]) for e in expenses)
    print(f"\nTotal spending: ₹{total:.2f}")


def view_by_category():
    expenses = read_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + float(e["amount"])

    print("\n--- Spending by Category ---")
    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat:<15}₹{amount:.2f}")


def delete_expense():
    view_expenses()
    expenses = read_expenses()
    if not expenses:
        return

    exp_id = input("\nEnter the ID of the expense to delete: ").strip()
    new_expenses = [e for e in expenses if e["id"] != exp_id]

    if len(new_expenses) == len(expenses):
        print("No expense found with that ID.")
        return

    with open(FILENAME, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(new_expenses)

    print(f"Expense {exp_id} deleted.")


def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Delete Expense")
    print("6. Exit")


def main():
    init_file()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye! Keep tracking those expenses. 💰")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
