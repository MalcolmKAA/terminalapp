from classes import Exercise, Workout
from functions import create_exercise, create_workout, show_workout_stats, save_workouts, load_workouts, export_stats_to_csv

def main():
    workouts = load_workouts()