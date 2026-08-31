import unittest
from habit import Habit

# Unit tests for the Habit class
class TestHabit(unittest.TestCase):

    # Test completing a daily habit
    def test_complete_daily_habit(self):
        habit = Habit("Exercise", "Go for a run", "daily")
        habit.complete()
        self.assertEqual(len(habit.completed_dates), 1)

    # Test that a daily habit cannot be completed twice on the same day
    def test_daily_habit_on_the_same_day(self):
        habit = Habit("Exercise", "Go for a run", "daily")
        habit.complete()
        habit.complete()  # Attempt to complete again on the same day
        self.assertEqual(len(habit.completed_dates), 1)  # Should still be 1

    # Test that a weekly habit cannot be completed twice in the same week
    def test_weekly_habit_on_the_same_week(self):
        habit = Habit("Clean room", "Clean the room", "weekly")
        habit.complete()
        habit.complete()  # Attempt to complete again in the same week
        self.assertEqual(len(habit.completed_dates), 1)  # Should still be 1
