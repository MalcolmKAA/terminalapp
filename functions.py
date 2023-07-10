import pickle
import csv
from classes import Exercise, Workout

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def create_exercise():
    while True:
        try:
            name = input("Enter exercise name: ")
            
            sets = input("Enter number of sets: ")
            while not sets.isdigit():
                print("Invalid input. Please try again.")
                sets = input("Enter number of sets: ")
            sets = int(sets)
            
            reps = input("Enter number of reps: ")
            while not reps.isdigit():
                print("Invalid input. Please try again.")
                reps = input("Enter number of reps: ")
            reps = int(reps)
            
            weight = input("Enter weight: ")
            while not is_float(weight):
                print("Invalid input. Please try again.")
                weight = input("Enter weight: ")
            weight = float(weight)
            
            rest_time = input("Enter rest time between sets in seconds: ")
            while not rest_time.isdigit():
                print("Invalid input. Please try again.")
                rest_time = input("Enter rest time between sets in seconds: ")
            rest_time = int(rest_time)
            
            weight_increase = input("Enter weight increase after successful completion: ")
            while not is_float(weight_increase):
                print("Invalid input. Please try again.")
                weight_increase = input("Enter weight increase after successful completion: ")
            weight_increase = float(weight_increase)
            
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


    


