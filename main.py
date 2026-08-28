from habit_repo import HabitRepo
from habit_tracker import HabitTracker
from cli import run_cli

repo = HabitRepo("habits.json")
tracker = HabitTracker(repo)

tracker.load()

run_cli(tracker)
