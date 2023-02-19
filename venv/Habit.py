import datetime


class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.frequency = frequency
        self.is_completed = False
        self.streak = 0
        self.last_completed_at = None
