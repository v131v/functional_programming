import random
import tkinter as tk


def filter_orders(orders, customer_id):
    return list(filter(lambda order: order["customer_id"] == customer_id, orders))


def total_order_amount(orders):
    return sum(map(lambda order: order["amount"], orders))


def average_order_cost(orders):
    if not orders:
        return 0
    return total_order_amount(orders) / len(orders)


def calculate_statistics():
    target_customer_id = int(entry_customer_id.get())
    filtered_orders = filter_orders(orders, target_customer_id)
    total_amount = total_order_amount(filtered_orders)
    average_cost = average_order_cost(filtered_orders)

    result_label.config(
        text=f"Orders for customer {target_customer_id}: {filtered_orders}\n"
        f"Total order amount: {total_amount}\n"
        f"Average order cost: {average_cost}"
    )


orders = [
    {
        "order_id": i + 1,
        "customer_id": random.randint(100, 110),
        "amount": round(random.uniform(50.0, 200.0), 2),
    }
    for i in range(50)
]

root = tk.Tk()
root.title("Order Statistics")

label_customer_id = tk.Label(root, text="Customer ID:")
entry_customer_id = tk.Entry(root)
calculate_button = tk.Button(
    root, text="Calculate Statistics", command=calculate_statistics
)
result_label = tk.Label(root, text="Results will appear here")

label_customer_id.pack()
entry_customer_id.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()
