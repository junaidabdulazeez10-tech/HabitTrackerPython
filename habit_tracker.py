from habit import Habit
from habit_repo import HabitRepo

# Manages the collection of habits.
class HabitTracker:
    def __init__(self, repo: HabitRepo):
        self.habits: list[Habit] = []
        self.repo = repo

    # Adds a new habit to the habits list.
    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    # Returns the list of habits.
    def get_habits(self) -> list[Habit]:
        return self.habits
    
    # Removes a habit from the habits list.
    def delete_habit(self, habit: Habit):
        self.habits.remove(habit)

    # Complete_habit method calls the complete method of the Habit class to mark a habit as completed.
    def complete_habit(self, habit: Habit):
        return habit.complete()
    
    # Updates the name, description, and frequency of a habit.
    def edit_habit(self, habit: Habit, name: str, description: str, frequency: str):
        habit.name = name
        habit.description = description
        habit.frequency = frequency

    # Saves the current list of habits to the repository.
    def save(self):
        self.repo.save_habits(self.habits)
        
    # Loads the list of habits from the repository and updates the habits list.
    def load(self):
        self.habits = self.repo.load_habits()
