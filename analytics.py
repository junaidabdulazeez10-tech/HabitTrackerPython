from datetime import timedelta

from habit import Habit

# Return all habits.
def get_all_habits(habits: list[Habit]) -> list[Habit]:
    return habits

# get_habits_by_frequency function filters the list of habits based on the specified frequency (daily or weekly) and returns the filtered list.
def get_habits_by_frequency(habits: list[Habit], frequency: str) -> list[Habit]:
    return list(filter(lambda habit: habit.frequency == frequency, habits))

# Calculate the longest consecutive streak for a single habit.
def get_longest_streak_for_habit(habit: Habit) -> int:
    sorted_dates = sorted(habit.completed_dates)

    if len(sorted_dates) == 0:
        return 0

    current_streak = 1
    longest_streak = 1

    for i in range(1, len(sorted_dates)):
        previous_date = sorted_dates[i - 1]
        current_date = sorted_dates[i]

        if habit.frequency == "daily":
            is_consecutive = current_date.date() == previous_date.date() + timedelta(
                days=1
            )

        elif habit.frequency == "weekly":
            previous_week = previous_date.date() - timedelta(
                days=previous_date.weekday()
            )

            current_week = current_date.date() - timedelta(days=current_date.weekday())

            is_consecutive = current_week == previous_week + timedelta(days=7)

        else:
            is_consecutive = False

        if is_consecutive:
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Calculate the longest streak across all habits.
def get_longest_streak(habits: list[Habit]) -> int:
    longest_streak = 0

    for habit in habits:
        streak = get_longest_streak_for_habit(habit)
        longest_streak = max(longest_streak, streak)

    return longest_streak
