from habit import Habit
from habit_tracker import HabitTracker
from analytics import (
    get_all_habits,
    get_habits_by_frequency,
    get_longest_streak_for_habit,
    get_longest_streak,
)

# Display the habits and let the user select one.
def select_habit(habits):
    for index, habit in enumerate(habits, start=1):
        print(index, "-", habit.name)

    try:
        habit_number = int(input("Choose a habit: "))

        if habit_number < 1 or habit_number > len(habits):
            print("Invalid habit number.")
            return None

        return habits[habit_number - 1]

    except ValueError:
        print("Please enter a number.")
        return None

# Ask the user for a valid daily or weekly frequency.
def get_frequency():
    frequency = input("Enter frequency (daily/weekly): ").strip().lower()

    if frequency not in ["daily", "weekly"]:
        print("Invalid frequency. Please enter daily or weekly.")
        return None

    return frequency

# Run the main command-line menu.
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
            frequency = get_frequency()

            if frequency is None:
                continue

            habit = Habit(name, description, frequency)

            tracker.add_habit(habit)
            tracker.save()

            print(f"Habit '{name}' created successfully.")

        elif choice == "3":
            habits = tracker.get_habits()

            if len(habits) == 0:
                print("No habits found.")
            else:
                habit = select_habit(habits)

                if habit is None:
                    continue

                completed = tracker.complete_habit(habit)
                if completed:
                    tracker.save()
                    print(f"Habit '{habit.name}' completed successfully.")
                else:
                    print(
                        f"Habit '{habit.name}' has already been completed for this period."
                    )

        elif choice == "4":
            habits = tracker.get_habits()

            if len(habits) == 0:
                print("No habits found.")
            else:
                habit = select_habit(habits)

                if habit is None:
                    continue

                new_name = input("Enter new habit name (leave blank to keep current): ")
                new_description = input(
                    "Enter new habit description (leave blank to keep current): "
                )
                new_frequency = (
                    input(
                        "Enter new frequency (daily/weekly) "
                        "(leave blank to keep current): "
                    )
                    .strip()
                    .lower()
                )

                if new_frequency:
                    if new_frequency not in ["daily", "weekly"]:
                        print("Invalid frequency. Please enter daily or weekly.")
                        continue
                else:
                    new_frequency = habit.frequency

                if not new_name:
                    new_name = habit.name

                if not new_description:
                    new_description = habit.description

                tracker.edit_habit(habit, new_name, new_description, new_frequency)

                tracker.save()

                print(f"Habit '{habit.name}' updated successfully.")

        elif choice == "5":

            habits = tracker.get_habits()

            if len(habits) == 0:
                print("No habits found.")
            else:
                habit = select_habit(habits)

                if habit is None:
                    continue

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
                frequency = get_frequency()

                if frequency is None:
                    continue

                habits = get_habits_by_frequency(tracker.get_habits(), frequency)

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
                    habit = select_habit(habits)

                    if habit is None:
                        continue

                    longest_streak = get_longest_streak_for_habit(habit)

                    unit = "days" if habit.frequency == "daily" else "weeks"

                    print(
                        f"Longest streak for '{habit.name}': "
                        f"{longest_streak} {unit}"
                    )

            elif analytics_choice == "4":
                longest_streak = get_longest_streak(tracker.get_habits())

                print(f"Longest streak overall: {longest_streak}")

            elif analytics_choice == "5":
                continue

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")
