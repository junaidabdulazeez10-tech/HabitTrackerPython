from habit import Habit


def get_all_habits(habits: list[Habit]) -> list[Habit]:
    return habits

def get_habits_by_frequency(habits: list[Habit], frequency: str) -> list[Habit]:
    return list(filter(lambda habit: habit.frequency == frequency, habits))

