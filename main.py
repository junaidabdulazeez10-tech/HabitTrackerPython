from habit import Habit
from habit_tracker import HabitTracker

daily_habit = Habit("Exercise", "do sport", "daily")
weekly_habit = Habit("Clean room", "clean your room man", "weekly")



tracker = HabitTracker()

tracker.complete_habit(daily_habit)

print(daily_habit.completed_dates)


