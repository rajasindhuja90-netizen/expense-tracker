# 💰 Expense Tracker (Python Mini Project)

A simple command-line **Expense Tracker** built in Python. It lets you record, view, and analyze your daily expenses, with all data saved automatically to a CSV file.

## Features
- ➕ Add an expense (category, description, amount, date)
- 📋 View all recorded expenses in a table
- 💵 View total spending
- 📊 View spending broken down by category
- 🗑️ Delete an expense by ID
- 💾 Data persists between runs using `expenses.csv`

## Tech Used
- Python 3 (standard library only — `csv`, `os`, `datetime`)

## Example Menu
```
===== EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Spending by Category
5. Delete Expense
6. Exit
```

## Project Structure
```
expense-tracker/
├── expense_tracker.py   # Main program
├── expenses.csv          # Auto-created to store your expense data
└── README.md              # Project documentation
```

## Possible Future Improvements
- Add monthly/weekly filtering
- Add data visualization (charts) using matplotlib
- Add a simple GUI using Tkinter
- Export summary reports to PDF
