# provide functions for analytics
# show all habits
# show habits with a certain frequency
# return the longest streak over all habits
# return the longest streak for a certain habit

import Habit
import sqlite3
from tabulate import tabulate


def display_table_habits():
    conn = sqlite3.connect('habits.db')
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habits = c.fetchall()
    conn.close()
    print(tabulate(habits, headers=["Name", "Created at", "Frequency", "Completed", "Ongoing streak", "Longest streak", "Last completed at"], tablefmt="grid"))
    # for Habit in habits:
    #    print("[{}] {}".format("X" if Habit.completed else " ", Habit.name))
