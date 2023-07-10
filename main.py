from classes import Exercise, Workout
from functions import create_exercise, create_workout, show_workout_stats, save_workouts, load_workouts, export_stats_to_csv, delete_workout

def main():
    workouts = load_workouts()
    while True:
        print("1. Create a new workout")
        print("2. Execute an existing workout")
        print("3. Stats")
        print("4. Export stats to CSV")
        print("5. Delete a workout")
        print("6. Save and exit")
        user_input = input("Choose an option: ")
        if user_input == "1":
            workouts.append(create_workout())
        elif user_input == "2":
            if not workouts:
                print("No workouts found. Please create a workout first.")
                continue
            for i, workout in enumerate(workouts):
                print(f"{i + 1}. {workout.name}")
            workout_number = int(input("Choose a workout to execute: ")) - 1
            if workout_number >= 0 and workout_number < len(workouts):
                workouts[workout_number].execute_workout()
        elif user_input == "3":
            show_workout_stats(workouts)
        elif user_input == "4":
            filename = input("Enter filename (or leave empty for 'workout_stats.csv'): ")
            if filename == "":
                filename = "workout_stats.csv"
            export_stats_to_csv(workouts, filename)
        elif user_input == "5":
            workouts = delete_workout(workouts)
        elif user_input == "6":
            print("Saving and exiting...")
            save_workouts(workouts)
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
