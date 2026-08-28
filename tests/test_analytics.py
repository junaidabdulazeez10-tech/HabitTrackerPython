import unittest
from datetime import datetime

from habit import Habit
from analytics import (
    get_longest_streak_for_habit,
    get_longest_streak,
    get_habits_by_frequency,
    get_all_habits,
)


class TestAnalytics(unittest.TestCase):

    def test_daily_longest_streak(self):
        habit = Habit("Exercise", "Daily exercise routine", "daily")
        habit.completed_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 2),
            datetime(2023, 1, 3),
            datetime(2023, 1, 5),
            datetime(2023, 1, 6),
        ]
        self.assertEqual(get_longest_streak_for_habit(habit), 3)

    def test_weekly_longest_streak(self):
        habit = Habit("Read", "Weekly reading habit", "weekly")
        habit.completed_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 8),
            datetime(2023, 1, 15),
            datetime(2023, 1, 29),
        ]
        self.assertEqual(get_longest_streak_for_habit(habit), 3)

    def test_longest_streak_across_all_habits(self):
        habit1 = Habit("Exercise", "Daily exercise routine", "daily")
        habit1.completed_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 2),
            datetime(2023, 1, 3),
            datetime(2023, 1, 4),
            datetime(2023, 1, 5),
            datetime(2023, 1, 6),
        ]

        habit2 = Habit("Read", "Weekly reading habit", "weekly")
        habit2.completed_dates = [
            datetime(2023, 1, 1),
            datetime(2023, 1, 8),
            datetime(2023, 1, 15),
            datetime(2023, 1, 29),
        ]

        habits = [habit1, habit2]
        self.assertEqual(get_longest_streak(habits), 6)

    def test_get_all_habits(self):
        habit1 = Habit("Exercise", "Exercise daily", "daily")
        habit2 = Habit("Clean", "Clean weekly", "weekly")

        habits = [habit1, habit2]

        result = get_all_habits(habits)

        self.assertEqual(result, habits)

    def test_get_habits_by_frequency(self):
        habit1 = Habit("Exercise", "Exercise daily", "daily")
        habit2 = Habit("Read", "Read daily", "daily")
        habit3 = Habit("Clean", "Clean weekly", "weekly")

        habits = [habit1, habit2, habit3]

        result = get_habits_by_frequency(habits, "daily")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].frequency, "daily")
        self.assertEqual(result[1].frequency, "daily")
