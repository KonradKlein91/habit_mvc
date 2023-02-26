import Habit
import sqlite3
from tabulate import tabulate


def display_table_habits():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habits = c.fetchall()
    conn.close()
    print(tabulate(habits, headers=["Name", "Created at", "Frequency", "Completed", "Ongoing streak", "Longest streak",
                                    "Last completed at"], tablefmt="grid"))


# TODO: to be tested and adjusted
def show_habits_frequency():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    frequency = input("Enter the frequency of the habit (e.g. daily, weekly, monthly): ")
    c.execute("SELECT * FROM habits WHERE frequency = ?", (frequency,))
    habits = c.fetchall()
    conn.close()
    print(tabulate(habits, headers=["Name", "Created at", "Frequency", "Completed", "Ongoing streak", "Longest streak",
                                    "Last completed at"], tablefmt="grid"))


# TODO: to be tested and adjusted
def show_all_streaks():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habits = c.fetchall()
    conn.close()
    print(tabulate(habits, headers=["Name", "Created at", "Frequency", "Completed", "Ongoing streak", "Longest streak",
                                    "Last completed at"], tablefmt="grid"))


# TODO: to be tested and adjusted
def show_habit_streak():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    name = input("Enter the name of the habit: ")
    c.execute("SELECT * FROM habits WHERE name = ?", (name,))
    habits = c.fetchall()
    conn.close()
    print(tabulate(habits, headers=["Name", "Created at", "Frequency", "Completed", "Ongoing streak", "Longest streak",
                                    "Last completed at"], tablefmt="grid"))
