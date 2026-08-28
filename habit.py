from datetime import datetime


class Habit:
    def __init__(self, name: str, description: str, frequency: str):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.created_at: datetime = datetime.now()
        self.completed_dates: list[datetime] = []

    def complete(self):
        today = datetime.now()

        for completed_date in self.completed_dates:

            if self.frequency == "daily":
                if completed_date.date() == today.date():
                    return False

            elif self.frequency == "weekly":
                if (
                    completed_date.isocalendar().year == today.isocalendar().year
                    and completed_date.isocalendar().week == today.isocalendar().week
                ):
                    return False

        self.completed_dates.append(today)
        return True
