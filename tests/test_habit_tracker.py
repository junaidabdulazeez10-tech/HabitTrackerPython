import unittest

from habit import Habit
from habit_repo import HabitRepo
from habit_tracker import HabitTracker

# Unit tests for the HabitTracker class
class TestHabitTracker(unittest.TestCase):

    # Test adding a habit to the tracker
    def test_add_habit(self):
        repo = HabitRepo("test_habits.json")
        tracker = HabitTracker(repo)
        habit = Habit("Exercise", "Go for a run", "daily")
        tracker.add_habit(habit)
        self.assertEqual(len(tracker.get_habits()), 1)

    # Test deleting a habit from the tracker
    def test_delete_habit(self):
        repo = HabitRepo("test_habits.json")
        tracker = HabitTracker(repo)
        habit = Habit("Exercise", "Go for a run", "daily")
        tracker.add_habit(habit)
        tracker.delete_habit(habit)
        self.assertEqual(len(tracker.get_habits()), 0)

    # Test editing a habit in the tracker
    def test_edit_habit(self):
        repo = HabitRepo("test_habits.json")
        tracker = HabitTracker(repo)
        habit = Habit("Exercise", "Go for a run", "daily")
        tracker.add_habit(habit)
        tracker.edit_habit(habit, "relax", "chill out", "weekly")
        self.assertEqual(habit.name, "relax")
        self.assertEqual(habit.description, "chill out")
        self.assertEqual(habit.frequency, "weekly")

    # Test completing a habit in the tracker
    def test_complete_habit(self):
        repo = HabitRepo("test_habits.json")
        tracker = HabitTracker(repo)
        habit = Habit("Exercise", "Go for a run", "daily")
        tracker.add_habit(habit)
        tracker.complete_habit(habit)
        self.assertEqual(len(habit.completed_dates), 1)
