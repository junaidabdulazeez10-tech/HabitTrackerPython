import json
from habit import Habit


class HabitRepo:
  def __init__(self, file: str):
    self.file = file

  def save_habits(self, habits: list[Habit]):
    habit_data_list = []

    for habit in habits:
      habit_data= {
        "name": habit.name,
        "description": habit.description,
        "frequency": habit.frequency,
        "created_at": habit.created_at.isoformat(),
        "completed_dates": [date.isoformat() for date in habit.completed_dates]
      }
      
      habit_data_list.append(habit_data)