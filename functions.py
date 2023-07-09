import pickle
import csv
from classes import Exercise, Workout

def create_exercise():
    name = input("Enter exercise name: ")
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of reps: "))
    weight = float(input("Enter weight: "))
    rest_time = int(input("Enter rest time between sets in seconds: "))
    weight_increase = float(input("Enter weight increase after successful completion: "))
    return Exercise(name, sets, reps, weight, rest_time, weight_increase)

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
    while True:
        for i, workout in enumerate(workouts, 1):
            print(f"{i}. {workout.name}")
        print("0. Back to main menu")

        user_input = input("Enter the number of the workout to view its stats: ")
        if user_input == "0":
            break
        else:
            selected_workout = workouts[int(user_input) - 1]
            selected_workout.show_stats()

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
