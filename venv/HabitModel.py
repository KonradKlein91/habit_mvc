import sqlite3
import datetime
import Habit


class HabitModel:
    def __init__(self):
        self.conn = sqlite3.connect('habits.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS habits (name text, created_at date, frequency int, is_completed int, streak int, last_completed_at text)")

    def add_habit(self, habit):
        self.conn.execute("INSERT INTO habits (name, created_at, frequency, is_completed, streak, last_completed_at) VALUES (?, ?, ?, ?, ?, ?)", (habit.name, habit.created_at, habit.frequency, habit.is_completed, habit.streak, habit.last_completed_at))
        self.conn.commit()

    def get_habits(self):
        cursor = self.conn.execute("SELECT * FROM habits")
        return [Habit(row[0], row[1] == 1) for row in cursor]

    def delete_habit(self, habit):
        self.conn.execute("DELETE FROM habits WHERE name = ?", (habit.name,))
        self.conn.commit()

    def complete_habit(self, habit):
        cursor = self.conn.execute("SELECT last_completed_at FROM habits WHERE name = ?", (habit.name,))
        last_completed_at_str = cursor.fetchone()[0]
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")
        if last_completed_at_str == today_str:
            return
        elif last_completed_at_str == '':
            streak = 1
        elif last_completed_at_str is not None and (
                datetime.datetime.now() - datetime.datetime.strptime(last_completed_at_str, "%Y-%m-%d")).days == 1:
            streak = habit.streak + 1
        else:
            streak = 1
        self.conn.execute("UPDATE habits SET is_completed = 1, streak = ?, last_completed_at = ? WHERE name = ?",
                          (streak, today_str, habit.name))
        self.conn.commit()

    def clear_database(self):
        self.conn.execute("DROP TABLE habits")
        self.conn.commit()