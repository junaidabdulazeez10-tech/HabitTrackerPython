# Habit Tracker

## Project Overview

This project is a command-line habit tracker developed in Python. It allows users to create, edit, delete, complete and view habits. Habits can be tracked on a daily or weekly basis.

The application also stores a history of habit completions and uses this data to calculate streaks.

## Features

- Create, edit and delete habits
- Complete daily or weekly habits
- Prevent duplicate completions within the same day or week
- View all habits
- Filter habits by frequency
- Calculate the longest streak for a specific habit
- Calculate the longest streak across all habits
- Store habit data in a JSON file
- Five predefined habits with four weeks of sample completion data

## Technologies Used

- Python
- JSON
- Python `unittest` framework

## Project Structure

```text
Habit_Tracker/
├── main.py
├── habit.py
├── habit_tracker.py
├── habit_repo.py
├── analytics.py
├── cli.py
├── habits.json
└── tests/
    ├── test_habit.py
    ├── test_habit_tracker.py
    ├── test_habit_repo.py
    └── test_analytics.py
```

## How to Run the Application

Make sure Python is installed on your computer.

Open a terminal in the project folder and run:

```bash
python main.py
```

The Habit Tracker menu will then be displayed:

```text
=== Habit Tracker ===
1. View habits
2. Create habit
3. Complete habit
4. Edit habit
5. Delete habit
6. View analytics
7. Quit
```

## How to Run the Tests

The project uses Python's built-in `unittest` framework.

Run all tests with:

```bash
python -m unittest discover -s tests -v
```

The project currently contains **13 passing unit tests**.

## Data Storage

Habit data is stored locally in `habits.json`. Each habit contains a name, description, frequency, creation date and a list of completed dates.

Each completion is stored as a timestamp in `completed_dates`. This completion history is used to calculate daily and weekly streaks.

The project includes **5 predefined habits with four weeks of sample completion data**.

## Testing

The tests are separated into four files:

- `test_habit.py` tests habit completion and duplicate completion prevention.
- `test_habit_tracker.py` tests adding, editing, deleting and completing habits.
- `test_habit_repo.py` tests saving and loading habit data using JSON.
- `test_analytics.py` tests filtering habits and calculating streaks.

**Current test result: 13 / 13 tests passing.**