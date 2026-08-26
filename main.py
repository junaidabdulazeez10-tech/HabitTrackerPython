from habit_repo import HabitRepo
from habit_tracker import HabitTracker

repo = HabitRepo("habits.json")
tracker = HabitTracker(repo)

tracker.load()

for habit in tracker.get_habits():
    print(habit.name, "-", habit.frequency)
    print("Completions:", len(habit.completed_dates))