from habit import Habit
class HabitTracker:
  def __init__(self):
    self.habits: list[Habit] = []  

  def add_habit(self, habit: Habit):
    self.habits.append(habit)
  
  def get_habits(self) -> list[Habit]:
    return self.habits

  def delete_habit(self, habit: Habit):
    self.habits.remove(habit)

  def complete_habit(self, habit: Habit): 
    habit.complete()

  def edit_habit(self, habit: Habit, name:str, description:str, frequency:str ):
    habit.name = name
    habit.description = description
    habit.frequency = frequency