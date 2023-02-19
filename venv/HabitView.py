import Habit


class HabitView:
    def show_habits(self, habits):
        for Habit in habits:
            print("[{}] {}".format("X" if Habit.completed else " ", Habit.name))

    def get_new_habit_info_from_user(self):
        name = input("Enter the name of the habit: ")
        frequency = input("Enter the frequency of the habit (e.g. daily, weekly, monthly): ")
        return Habit.Habit(name, frequency)

    def get_habit_from_user(self):
        name = input("Enter the name of the habit: ")
        return Habit(name)
