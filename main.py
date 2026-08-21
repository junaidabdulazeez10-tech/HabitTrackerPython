from habit import Habit

habit = Habit("Exercise", "do sport", "daily")

print("Before:", habit.completed_dates)

habit.complete()

print("After first:", habit.completed_dates)

habit.complete()

print("After second:", habit.completed_dates)