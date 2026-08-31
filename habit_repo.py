import json
from habit import Habit
from datetime import datetime

# Handles saving and loading habits from a JSON file.
class HabitRepo:
    def __init__(self, file: str):
        self.file = file

    # Save habits to JSON and convert datetime values to ISO strings.
    def save_habits(self, habits: list[Habit]):
        habit_data_list = []

        for habit in habits:
            habit_data = {
                "name": habit.name,
                "description": habit.description,
                "frequency": habit.frequency,
                "created_at": habit.created_at.isoformat(),
                "completed_dates": [date.isoformat() for date in habit.completed_dates],
            }

            habit_data_list.append(habit_data)

        with open(self.file, "w") as file:
            json.dump(habit_data_list, file, indent=2)

    # Load habits from JSON and convert ISO strings back to datetime values.
    def load_habits(self) -> list[Habit]:
        try:
            with open(self.file, "r") as file:
                habit_data_list = json.load(file)
        except FileNotFoundError:
            return []

        habits = []
        for habit_data in habit_data_list:
            habit = Habit(
                name=habit_data["name"],
                description=habit_data["description"],
                frequency=habit_data["frequency"],
            )
            habit.created_at = datetime.fromisoformat(habit_data["created_at"])
            habit.completed_dates = [
                datetime.fromisoformat(date) for date in habit_data["completed_dates"]
            ]
            habits.append(habit)

        return habits
