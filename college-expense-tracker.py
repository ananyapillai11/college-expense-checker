import tkinter as tk
from tkinter import messagebox

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

class CollegeExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("College Expense Tracker")

        self.expenses = []

        self.center_frame = tk.Frame(root, borderwidth=2, relief="solid", bg="light pink")
        self.center_frame.pack(expand=True, padx=55, pady=55)

        self.category_label = tk.Label(self.center_frame, text="Expense Category:", font=("Helvetica", 50), bg="light pink")
        self.category_label.pack(anchor="center")

        self.category_entry = tk.Entry(self.center_frame, font=("Helvetica", 50))
        self.category_entry.pack(anchor="center")

        self.amount_label = tk.Label(self.center_frame, text="Expense Amount (INR):", font=("Helvetica", 50), bg="light pink")
        self.amount_label.pack(anchor="center")

        self.amount_entry = tk.Entry(self.center_frame, font=("Helvetica", 50))
        self.amount_entry.pack(anchor="center")

        self.add_button = tk.Button(self.center_frame, text="Add Expense", command=self.add_expense, bg="green", fg="white", font=("Helvetica", 50))
        self.add_button.pack(anchor="center")

        self.summary_button = tk.Button(self.center_frame, text="Display Summary", command=self.display_summary, bg="blue", fg="white", font=("Helvetica", 50))
        self.summary_button.pack(anchor="center")

    def add_expense(self):
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())

        expense = Expense(category, amount)
        self.expenses.append(expense)

        messagebox.showinfo("Expense Added", "Expense has been added.")

        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def calculate_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def display_summary(self):
        summary = "College Expense Summary:\n"
        for expense in self.expenses:
            summary += f"{expense.category}: ₹{expense.amount:.2f}\n"
        total = self.calculate_total_expenses()
        summary += f"Total Expenses: ₹{total:.2f}"

        messagebox.showinfo("Expense Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeExpenseTrackerGUI(root)
    root.mainloop()
