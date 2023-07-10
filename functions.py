import pickle
import csv
from classes import Exercise, Workout

def create_exercise():
    name = input("Enter exercise name: ")

    while True:
        try:
            sets = int(input("Enter number of sets: "))
            if sets <= 0:
                print("Number of sets must be greater than 0.")
                continue

            reps = int(input("Enter number of reps: "))
            if reps < 0:
                print("Number of reps must 0 or greater.")
                continue

            weight = float(input("Enter weight: "))
            if weight <= 0:
                print("Weight must be greater than 0.")
                continue

            rest_time = int(input("Enter rest time between sets in seconds: "))
            if rest_time < 0:
                print("Rest time must be 0 or greater.")
                continue

            weight_increase = float(input("Enter weight increase after successful completion: "))
            if weight_increase < 0:
                print("Weight increase must be 0 or greater.")
                continue

            return Exercise(name, sets, reps, weight, rest_time, weight_increase)

        except ValueError:
            print("Invalid input. Please try again.")


def create_workout():
    name = input("Enter workout name: ")
    exercises = []
    while True:
        exercises.append(create_exercise())
        add_more = input("Do you want to add more exercises to this workout? (yes/no): ")
        if add_more.lower() != "yes":
            break
    return Workout(name, exercises)

def show_workout_stats(workouts):
    if not workouts:
        print("No workouts found.")
        return

    while True:
        print("0. Back to main menu")
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout.name}")

        user_input = input("Enter the number of the workout to view its stats: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if user_input == 0:
            return
        elif user_input > 0 and user_input <= len(workouts):
            selected_workout = workouts[user_input - 1]
            selected_workout.show_stats()
            return
        else:
            print("Invalid option. Please try again.")


def save_workouts(workouts):
    with open('workouts.pkl', 'wb') as f:
        pickle.dump(workouts, f)

def load_workouts():
    try:
        with open('workouts.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def export_stats_to_csv(workouts, filename="workout_stats.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Workout', 'Exercise', 'Max Weight Lifted', 'Date Max Weight Lifted']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for workout in workouts:
            for exercise in workout.exercises:
                writer.writerow({
                    'Workout': workout.name, 
                    'Exercise': exercise.name, 
                    'Max Weight Lifted': exercise.max_weight, 
                    'Date Max Weight Lifted': exercise.date_max_weight
                })
def delete_workout(workouts):
    if not workouts:
        print("No workouts found.")
        return workouts

    while True:
        for i, workout in enumerate(workouts):
            print(f"{i + 1}. {workout.name}")
        print("0. Go back")

        try:
            workout_number = int(input("Choose a workout to delete or 0 to go back: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if workout_number > 0 and workout_number <= len(workouts):
            del workouts[workout_number-1]
            print("Workout deleted successfully.")
            break
        elif workout_number == 0:
            print("Operation cancelled.")
            break
        else:
            print("Invalid option. Please try again.")

    return workouts


    


