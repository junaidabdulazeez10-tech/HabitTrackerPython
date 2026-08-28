from habit import Habit
from habit_repo import HabitRepo


class HabitTracker:
    def __init__(self, repo: HabitRepo):
        self.habits: list[Habit] = []
        self.repo = repo

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def get_habits(self) -> list[Habit]:
        return self.habits

    def delete_habit(self, habit: Habit):
        self.habits.remove(habit)

    def complete_habit(self, habit: Habit):
        return habit.complete()

    def edit_habit(self, habit: Habit, name: str, description: str, frequency: str):
        habit.name = name
        habit.description = description
        habit.frequency = frequency

    def save(self):
        self.repo.save_habits(self.habits)

    def load(self):
        self.habits = self.repo.load_habits()
