import sqlite3
import datetime
import Habit


class HabitModel:
    def __init__(self):
        self.conn = sqlite3.connect('habits.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS habits (name text, created_at date, frequency int, is_completed int, ongoing_streak int, longest_streak int, last_completed_at text)")

# TODO: add error handling if the name of the habit already exists
    def add_habit(self, habit):
        self.conn.execute("INSERT INTO habits (name, created_at, frequency, is_completed, ongoing_streak, longest_streak, last_completed_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (habit.name, habit.created_at, habit.frequency, habit.is_completed, habit.ongoing_streak, habit.longest_streak, habit.last_completed_at))
        self.conn.commit()

    def delete_habit(self, habit):
        self.conn.execute("DELETE FROM habits WHERE name = ?", (habit.name,))
        self.conn.commit()

    def complete_habit(self, habit):

        # get the last_completed_at date from the database
        cursor = self.conn.execute("SELECT last_completed_at FROM habits WHERE name = ?", (habit.name,))
        last_completed_at_str = cursor.fetchone()[0]

        # get the ongoing_streak from the database
        cursor = self.conn.execute("SELECT ongoing_streak FROM habits WHERE name = ?", (habit.name,))
        ongoing_streak = cursor.fetchone()[0]

        # get the longest_streak from the database
        cursor = self.conn.execute("SELECT longest_streak FROM habits WHERE name = ?", (habit.name,))
        longest_streak = cursor.fetchone()[0]

        # get the current date in string format
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")

        # compare the last_completed_at date with the current date
        if last_completed_at_str == today_str:
            return # do nothing if the habit has already been completed today

        # update the ongoing_streak and longest_streak if last_completed_at is empty
        elif last_completed_at_str == '':
            ongoing_streak = 1

        # update the ongoing_streak and longest_streak if last_completed_at is older than 1 day
        # TODO: fix that the frequency is dynamic and not hardcoded to 1 day
        elif last_completed_at_str is not None and (
                datetime.datetime.now() - datetime.datetime.strptime(last_completed_at_str, "%Y-%m-%d")).days == 1:
            ongoing_streak = ongoing_streak + 1


        else:
            ongoing_streak = 1

        if ongoing_streak > longest_streak:
            longest_streak = ongoing_streak
        else:
            longest_streak = longest_streak

        self.conn.execute("UPDATE habits SET is_completed = 1, ongoing_streak = ?, longest_streak = ?, last_completed_at = ? WHERE name = ?",
                          (ongoing_streak, longest_streak, today_str, habit.name))
        self.conn.commit()