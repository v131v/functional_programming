import random
from functools import reduce


def filter_students(students, target_ages=None, target_subjects=None):
    filtered_students = students.copy()

    if target_ages:
        filtered_students = filter(
            lambda student: student["age"] in target_ages, students
        )

    if target_subjects:
        filtered_students = filter(
            lambda student: all(
                map(lambda grade: grade in student["grades"], target_subjects)
            ),
            students,
        )

    return filtered_students


def calculate_student_average(grades):
    return sum(grades) / len(grades) if grades else 0


def calculate_total_average(students):
    grades_sum = reduce(lambda s, student: s + sum(student["grades"]), students, 0)
    return grades_sum / (4 * len(students))


def aggregate_students_with_highest_mark(students):
    highest_average = max(
        map(lambda student: calculate_student_average(student["grades"]), students)
    )

    aggregated_students = filter(
        lambda student: calculate_student_average(student["grades"]) == highest_average,
        students,
    )
    return aggregated_students


students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 23, "grades": [75, 85, 80, 88]},
    {"name": "Emily", "age": 20, "grades": [92, 91, 89, 94]},
    {"name": "Frank", "age": 22, "grades": [78, 82, 86, 90]},
    {"name": "Grace", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Harry", "age": 23, "grades": [90, 92, 91, 94]},
    {"name": "Ivy", "age": 20, "grades": [88, 87, 89, 92]},
    {"name": "Jack", "age": 22, "grades": [76, 78, 80, 85]},
    {"name": "Katherine", "age": 21, "grades": [92, 94, 91, 95]},
    {"name": "Leo", "age": 23, "grades": [85, 88, 89, 92]},
    {"name": "Mia", "age": 20, "grades": [90, 91, 88, 92]},
    {"name": "Noah", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Olivia", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "Peter", "age": 23, "grades": [75, 85, 80, 88]},
    {"name": "Quinn", "age": 20, "grades": [92, 91, 89, 94]},
    {"name": "Ryan", "age": 22, "grades": [78, 82, 86, 90]},
    {"name": "Sophia", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Thomas", "age": 23, "grades": [90, 92, 91, 94]},
    {"name": "Ursula", "age": 20, "grades": [88, 87, 89, 92]},
    {"name": "Victor", "age": 22, "grades": [76, 78, 80, 85]},
    {"name": "Wendy", "age": 21, "grades": [92, 94, 91, 95]},
    {"name": "Xander", "age": 23, "grades": [85, 88, 89, 92]},
    {"name": "Yasmine", "age": 20, "grades": [90, 91, 88, 92]},
    {"name": "Zane", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Abigail", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "Benjamin", "age": 23, "grades": [75, 85, 80, 88]},
    {"name": "Catherine", "age": 20, "grades": [92, 91, 89, 94]},
    {"name": "Daniel", "age": 22, "grades": [78, 82, 86, 90]},
    {"name": "Ella", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Finn", "age": 23, "grades": [90, 92, 91, 94]},
    {"name": "Giselle", "age": 20, "grades": [88, 87, 89, 92]},
    {"name": "Henry", "age": 22, "grades": [76, 78, 80, 85]},
    {"name": "Isabel", "age": 21, "grades": [92, 94, 91, 95]},
    {"name": "Jason", "age": 23, "grades": [85, 88, 89, 92]},
    {"name": "Kelsey", "age": 20, "grades": [90, 91, 88, 92]},
    {"name": "Liam", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Megan", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "Nathan", "age": 23, "grades": [75, 85, 80, 88]},
    {"name": "Oliver", "age": 20, "grades": [92, 91, 89, 94]},
    {"name": "Penelope", "age": 22, "grades": [78, 82, 86, 90]},
    {"name": "Quincy", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Rebecca", "age": 23, "grades": [90, 92, 91, 94]},
    {"name": "Samuel", "age": 20, "grades": [88, 87, 89, 92]},
    {"name": "Tessa", "age": 22, "grades": [76, 78, 80, 85]},
    {"name": "Ulysses", "age": 21, "grades": [92, 94, 91, 95]},
    {"name": "Vivian", "age": 23, "grades": [85, 88, 89, 92]},
    {"name": "William", "age": 20, "grades": [90, 91, 88, 92]},
    {"name": "Xena", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Yuri", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "Zachary", "age": 23, "grades": [75, 85, 80, 88]},
]

for student in students:
    student["grades"] = [random.randint(65, 100) for _ in student["grades"]]
