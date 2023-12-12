import random
import tkinter as tk
from tkinter import ttk


def filter_users_by_expenses(users, threshold):
    filtered_users = [user for user in users if sum(user["expenses"]) > threshold]
    return filtered_users


def calculate_total_expenses_per_user(user):
    return sum(user["expenses"])


def calculate_total_expenses_all_users(users):
    total_expenses = sum(sum(user["expenses"]) for user in users)
    return total_expenses


def update_results():
    threshold = int(entry_threshold.get())
    filtered_users = filter_users_by_expenses(users, threshold)

    result_text.delete(1.0, tk.END)

    for user in filtered_users:
        total_expenses_per_user = calculate_total_expenses_per_user(user)
        result_text.insert(
            tk.END, f"{user['name']} - Total thresholds: {total_expenses_per_user}\n"
        )

    total_expenses_all_users = calculate_total_expenses_all_users(filtered_users)
    result_text.insert(
        tk.END, f"\nTotal thresholds of all users: {total_expenses_all_users}"
    )


root = tk.Tk()
root.title("Lab2")

label_threshold = tk.Label(root, text="Minimal thresholds sum:")
label_threshold.grid(row=0, column=0, padx=10, pady=10)

entry_threshold = ttk.Entry(root)
entry_threshold.grid(row=0, column=1, padx=10, pady=10)

button_filter = ttk.Button(root, text="Filter", command=update_results)
button_filter.grid(row=0, column=2, padx=10, pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

users = [
    {"name": f"User{i+1}", "expenses": [random.randint(0, 1000) for _ in range(4)]}
    for i in range(50)
]


root.mainloop()
