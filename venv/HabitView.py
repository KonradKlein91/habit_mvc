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
            choice = input("enter your choice: ")
            if choice == "1":
                self.add_habit()
            elif choice == "2":
                self.delete_habit()
            elif choice == "3":
                print("tbd")
            elif choice == "4":
                self.show_habits()
            elif choice == "5":
                print("tbd")
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_main_menu(self):
        print("-----------------------")
        print("1. add a new habit")
        print("2. delete a habit")
        print("3. complete a habit")
        print("4. show all habits")
        print("5. show longest streaks")
        print("6. show longest streak for a habit")
        print("7. show habits with certain frequency")
        print("8. insert sample data")
        print("9. clear database")
        print("q. quit")
        print("-----------------------")

    def add_habit(self):
        Habit = self.get_new_habit_info_from_user()
        self.controller.add_habit(Habit)

    def delete_habit(self):
        self.controller.delete_habit()

    def show_habits(self):
        # habits = self.model.get_habits()
        self.controller.show_habits()

    def show_habits_frequency(self):
        # habits = self.model.get_habits()
        show_habits_frequency()

    def complete_habit(self, Habit):
        self.model.complete_habit(Habit)

    def get_new_habit_info_from_user(self):
        name = input("enter the name of the habit: ")
        frequency = input("enter the frequency of the habit (e.g. daily, weekly, monthly): ")
        return Habit(name, frequency)

    def get_habit_from_user(self):
        name = input("enter the name of the habit: ")
        return Habit(name)