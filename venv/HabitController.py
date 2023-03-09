from HabitModel import HabitModel
from Habit import Habit
from Analytics import *


class HabitController:
    def __init__(self):
        self.model = HabitModel()

    def add_habit(self, Habit):
        # Habit = self.view.get_new_habit_info_from_user()
        self.model.add_habit(Habit)

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


# if __name__ == '__main__':
#     controller = HabitController()
#     while True:
#         print("1. Add habit")
#         print("2. Show habits")
#         print("3. Complete habit")
#         print("4. Delete habit")
#         print("5. Clear database")
#         print("6. Show habits with certain frequency")
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             controller.add_habit()
#         elif choice == 2:
#             controller.show_habits()
#         elif choice == 3:
#             habits = controller.model.get_habits()
#             for i, habit in enumerate(habits):
#                 print("{}. {}".format(i + 1, habit.name))
#             index = int(input("Enter the number of the habit to complete: ")) - 1
#             if 0 <= index < len(habits):
#                 controller.complete_habit(habits[index])
#         elif choice == 4:
#             habits = controller.model.get_habits()
#             for i, habit in enumerate(habits):
#                 print("{}. {}".format(i + 1, habit.name))
#             index = int(input("Enter the number of the habit to delete: ")) - 1
#             if 0 <= index < len(habits):
#                 controller.delete_habit(habits[index])
#         elif choice == 5:
#             controller.clear_database()
#         elif choice == 6:
#             controller.show_habits_frequency()
#         else:
#             break
#     controller.model.conn.close()
