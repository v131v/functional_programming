import tkinter as tk
from tkinter import messagebox
from lib import *

student_avgs = []
filtered_students = []

# Создание основного окна
root = tk.Tk()
root.title("Lab1")

# Создание строковых полей
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)


def get_data(entry):
    return map(int, entry.get().split(" "))


def handler1():
    global students
    global filtered_students
    filtered_students = filter_students(students, get_data(entry1), get_data(entry2))
    messagebox.showinfo("Filtered", filtered_students)


def handler2():
    global filtered_students
    global student_avgs
    student_avgs = map(
        lambda student: calculate_student_average(student["grades"]), filter_students
    )

    total_avg = calculate_total_average(filtered_students)
    messagebox.showinfo(f"Total avg: {total_avg}", student_avgs)


def handler3():
    global filtered_students
    global student_avgs
    highest_avg_students = aggregate_students_with_highest_mark(filtered_students)
    messagebox.showinfo(f"Aggregated max: {max(student_avgs)}", highest_avg_students)


# Создание кнопок
button_filter = tk.Button(
    root,
    text="Filter",
    command=handler1,
)
button_avg = tk.Button(root, text="Average", command=handler2)
button_aggregate = tk.Button(root, text="Aggregate", command=handler3)


# Размещение элементов в столбик по центру
entry1.pack(pady=5)
entry2.pack(pady=5)
button_filter.pack(pady=5)
button_avg.pack(pady=5)
button_aggregate.pack(pady=5)

# Запуск главного цикла
root.mainloop()
