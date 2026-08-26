import unittest
import os

from habit import Habit
from habit_repo import HabitRepo

class TestHabitRepo(unittest.TestCase):

  def test_save_and_load_habits(self):

    repo = HabitRepo("test_habits.json")
    habit = Habit("Exercise", "Go for a run", "daily")

    habit.complete()
    repo.save_habits([habit])
    loaded_habits = repo.load_habits()

    self.assertEqual(len(loaded_habits), 1)
    self.assertEqual(loaded_habits[0].name, "Exercise")
    self.assertEqual(loaded_habits[0].description, "Go for a run")
    self.assertEqual(loaded_habits[0].frequency, "daily")
    self.assertEqual(len(loaded_habits[0].completed_dates), 1)

    os.remove("test_habits.json")