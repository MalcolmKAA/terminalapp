import datetime
from time import sleep

class Exercise:
    def __init__(self, name, sets, reps, weight, rest_time, weight_increase):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.rest_time = rest_time
        self.weight_increase = weight_increase
        self.max_weight = weight
        self.date_max_weight = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        def increase_weight(self):
        self.weight += self.weight_increase
        if self.weight > self.max_weight:
            self.max_weight = self.weight
            self.date_max_weight = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        def decrease_weight(self, decrease_amount):
        self.weight -= decrease_amount
        if self.weight < 0:
            self.weight = 0

class Workout:
    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def execute_workout(self):
        for exercise in self.exercises:
            print(f"Starting {exercise.name}...")
            all_sets_successful = True
            for set_number in range(1, exercise.sets + 1):
                print(f"Set {set_number} of {exercise.sets}. {exercise.reps} reps at {exercise.weight}KG. Type 'exit' at anytime to leave the workout.")
                user_input = input("Press 1 if completed, press 2 if failed: ")
                if user_input == "1":
                    print(f"Congratulations! Rest for {exercise.rest_time} seconds before next set.")
                    sleep(exercise.rest_time)
                elif user_input == "2":
                    all_sets_successful = False
                    print(f"You failed the set. Would you like to decrease weight? ")
                    user_input = input("Press 1 for yes, 2 for no: ")
                    if user_input == "1":
                        decrease_amount = int(input("Enter decrease amount: "))
                        exercise.decrease_weight(decrease_amount)
                        print(f"Weight has been decreased by {decrease_amount}. New weight is {exercise.weight}.")
                elif user_input.lower() == "exit":
                    print("Exiting the workout...")
                    return
            if all_sets_successful:
                print(f"You have successfully completed {exercise.name}! Weight will be increased by {exercise.weight_increase} for next workout.")
                exercise.increase_weight()