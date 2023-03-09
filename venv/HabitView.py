from Habit import Habit
from HabitController import HabitController
from HabitModel import HabitModel


class HabitView:
    def __init__(self):
        self.controller = HabitController()
        self.model = HabitModel()

    def run(self):
        while True:
            self.show_main_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_habit()
            elif choice == "2":
                self.list_habits()
            elif choice == "3":
                self.complete_habit()
            elif choice == "4":
                self.analytics()
            elif choice == "5":
                self.clear_database()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_main_menu(self):
        print("Habit Tracker Main Menu")
        print("-----------------------")
        print("1. Add a new habit")
        print("2. List all habits")
        print("3. Mark a habit as completed")
        print("4. Analytics")
        print("5. Clear database")
        print("q. Quit")

    def add_habit(self):
        Habit = self.get_new_habit_info_from_user()
        self.controller.add_habit(Habit)

    def delete_habit(self, Habit):
        self.model.delete_habit(Habit)

    def show_habits(self):
        # habits = self.model.get_habits()
        display_table_habits()

    def show_habits_frequency(self):
        # habits = self.model.get_habits()
        show_habits_frequency()

    def complete_habit(self, Habit):
        self.model.complete_habit(Habit)

    def get_new_habit_info_from_user(self):
        name = input("Enter the name of the habit: ")
        frequency = input("Enter the frequency of the habit (e.g. daily, weekly, monthly): ")
        return Habit(name, frequency)

    def get_habit_from_user(self):
        name = input("Enter the name of the habit: ")
        return Habit(name)