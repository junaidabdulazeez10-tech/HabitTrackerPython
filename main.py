from habit_repo import HabitRepo

repo = HabitRepo("habits.json")

habits = repo.load_habits()

for habit in habits:
    print("Name:", habit.name)
    print("Description:", habit.description)
    print("Frequency:", habit.frequency)
    print("Created:", habit.created_at)
    print("Completed:", habit.completed_dates)
    print()