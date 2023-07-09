from classes import Exercise, Workout
from functions import create_exercise, create_workout, show_workout_stats, save_workouts, load_workouts, export_stats_to_csv

def main():
    workouts = load_workouts()
    while True:
        print("1. Create a new workout")
        print("2. Execute an existing workout")
        print("3. Stats")
        print("4. Export stats to CSV")
        print("5. Save and exit")
        user_input = input("Choose an option: ")