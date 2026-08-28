from habit import Habit
from habit_tracker import HabitTracker
from analytics import (
    get_all_habits,
    get_habits_by_frequency,
    get_longest_streak_for_habit,
    get_longest_streak
)


def run_cli(tracker: HabitTracker):
    while True:
        print("\n=== Habit Tracker ===")
        print("1. View habits")
        print("2. Create habit")
        print("3. Complete habit")
        print("4. Edit habit")
        print("5. Delete habit")
        print("6. View analytics")
        print("7. Quit")

        choice = input("Choose an option: ")
        print()

        if choice == "1":
           habits = tracker.get_habits()

           if len(habits) == 0:
              print("No habits found.")

           else:
              for habit in habits:
                print(habit.name, "-", habit.frequency)

        elif choice == "2":
          name = input("Enter habit name: ")
          description = input("Enter habit description: ")
          frequency = input("Enter frequency (daily/weekly): ")

          habit = Habit(name, description, frequency)

          tracker.add_habit(habit)
          tracker.save()

          print(f"Habit '{name}' created successfully.")

        elif choice == "3":
          habits = tracker.get_habits()

          if len(habits) == 0:
            print("No habits found.")
          else:
              for index, habit in enumerate(habits, start=1):
                  print(index, "-", habit.name)

              habit_number = int(input("Choose a habit to complete: "))
              habit = habits[habit_number - 1]

              completed = tracker.complete_habit(habit)
              if completed:
                    tracker.save()
                    print(f"Habit '{habit.name}' completed successfully.")
              else:
                    print(f"Habit '{habit.name}' has already been completed for this period.")

        elif choice == "4":
          habits = tracker.get_habits()

          if len(habits) == 0:
              print("No habits found.")
          else:
              for index, habit in enumerate(habits, start=1):
                  print(index, "-", habit.name)

              habit_number = int(input("Choose a habit to edit: "))
              habit = habits[habit_number - 1]

              new_name = input("Enter new habit name (leave blank to keep current): ")
              new_description = input("Enter new habit description (leave blank to keep current): ")
              new_frequency = input("Enter new frequency (daily/weekly) (leave blank to keep current): ")

              if not new_name:
                  new_name = habit.name

              if not new_description:
                  new_description = habit.description

              if not new_frequency:
                  new_frequency = habit.frequency

              tracker.edit_habit(
                  habit,
                  new_name,
                  new_description,
                  new_frequency
              )

              tracker.save()

              print(f"Habit '{habit.name}' updated successfully.")

        elif choice == "5":

          habits = tracker.get_habits()

          if len(habits) == 0:
              print("No habits found.")
          else:
              for index, habit in enumerate(habits, start=1):
                  print(index, "-", habit.name)

              habit_number = int(input("Choose a habit to delete: "))
              habit = habits[habit_number - 1]

              tracker.delete_habit(habit)
              tracker.save()

              print(f"Habit '{habit.name}' deleted successfully.")


        
        elif choice == "6":
          
            print("=== Analytics ===")
            print("1. View all habits")
            print("2. View habits by frequency")
            print("3. View longest streak for a habit")
            print("4. View longest streak overall")
            print("5. Back to main menu")

            analytics_choice = input("Choose an option: ")
            print()

            if analytics_choice == "1":
                habits = get_all_habits(tracker.get_habits())

                if len(habits) == 0:
                    print("No habits found.")
                else:
                    for habit in habits:
                        print(habit.name, "-", habit.frequency)

            elif analytics_choice == "2":
                frequency = input("Enter frequency (daily/weekly): ")

                habits = get_habits_by_frequency(
                    tracker.get_habits(),
                    frequency
                )

                if len(habits) == 0:
                    print(f"No {frequency} habits found.")
                else:
                    for habit in habits:
                        print(habit.name, "-", habit.frequency)

            elif analytics_choice == "3":
                habits = tracker.get_habits()

                if len(habits) == 0:
                    print("No habits found.")
                else:
                    for index, habit in enumerate(habits, start=1):
                        print(index, "-", habit.name)

                    habit_number = int(
                        input("Choose a habit to view longest streak: ")
                    )

                    habit = habits[habit_number - 1]

                    longest_streak = get_longest_streak_for_habit(habit)

                    unit = "days" if habit.frequency == "daily" else "weeks"

                    print(
                        f"Longest streak for '{habit.name}': "
                        f"{longest_streak} {unit}"
                    )

            elif analytics_choice == "4":
                longest_streak = get_longest_streak(
                    tracker.get_habits()
                )

                print(f"Longest streak overall: {longest_streak}")

            elif analytics_choice == "5":
                continue

        elif choice == "7":
          print("Goodbye!")
          break

        else:
          print("Invalid option. Please choose between 1 and 7.")