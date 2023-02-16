import sqlite3
import datetime

class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.frequency = frequency
        self.is_completed = False
        self.streak = 0
        self.last_completed_at = None

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

class HabitView:
    def show_habits(self, habits):
        for habit in habits:
            print("[{}] {}".format("X" if habit.completed else " ", habit.name))

    def get_new_habit_info_from_user(self):
        name = input("Enter the name of the habit: ")
        frequency = input("Enter the frequency of the habit (e.g. daily, weekly, monthly): ")
        return Habit(name, frequency)

    def get_habit_from_user(self):
        name = input("Enter the name of the habit: ")
        return Habit(name)

class HabitController:
    def __init__(self):
        self.model = HabitModel()
        self.view = HabitView()

    def add_habit(self):
        habit = self.view.get_new_habit_info_from_user()
        self.model.add_habit(habit)

    def delete_habit(self, habit):
        self.model.delete_habit(habit)

    def show_habits(self):
        habits = self.model.get_habits()
        self.view.show_habits(habits)

    def complete_habit(self, habit):
        self.model.complete_habit(habit)

if __name__ == '__main__':
    controller = HabitController()
    while True:
        print("1. Add habit")
        print("2. Show habits")
        print("3. Complete habit")
        print("4. Delete habit")
        print("5. Clear database")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            controller.add_habit()
        elif choice == 2:
            controller.show_habits()
        elif choice == 3:
            habits = controller.model.get_habits()
            for i, habit in enumerate(habits):
                print("{}. {}".format(i + 1, habit.name))
            index = int(input("Enter the number of the habit to complete: ")) - 1
            if 0 <= index < len(habits):
                controller.complete_habit(habits[index])
        elif choice == 4:
            habits = controller.model.get_habits()
            for i, habit in enumerate(habits):
                print("{}. {}".format(i + 1, habit.name))
            index = int(input("Enter the number of the habit to delete: ")) - 1
            if 0 <= index < len(habits):
                controller.delete_habit(habits[index])
        elif choice == 5:
            controller.model.clear_database()
        else:
            break
    controller.model.conn.close()
