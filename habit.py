from datetime import datetime
class Habit:
  def __init__(self, name: str, description:str , frequency: str):
    self.name = name
    self.description = description
    self.frequency = frequency
    self.created_at: datetime = datetime.now()
    self.completed_dates: list[datetime] = []

  def complete(self):
    today_date = datetime.now().date()
    
    for completed_date in self.completed_dates:
      if(completed_date.date() == today_date):
        return
      
    self.completed_dates.append(datetime.now())
  