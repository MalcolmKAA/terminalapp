import unittest
from unittest.mock import patch
from datetime import date
from classes import Workout, Exercise

class TestWorkoutCreation(unittest.TestCase):
    def test_create_workout(self):
        workout = Workout("Test Workout", [])
        self.assertEqual(workout.name, "Test Workout")

    def test_create_exercise(self):
        exercise = Exercise("Bench Press", 5, 5, 50, 30, 5)
        self.assertEqual(exercise.name, "Bench Press")
        self.assertEqual(exercise.sets, 5)
        self.assertEqual(exercise.reps, 5)
        self.assertEqual(exercise.weight, 50)
        self.assertEqual(exercise.rest_time, 30)
        self.assertEqual(exercise.weight_increase, 5)

class TestWorkoutExecution(unittest.TestCase):
    def setUp(self):
        self.test_exercise = Exercise("Test Exercise", 5, 5, 20.0, 2, 2.5)

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1'])
    def test_execute_workout_successful(self, mock_input):
        workout = Workout("Test workout", [self.test_exercise])
        workout.execute_workout()
        self.assertEqual(workout.exercises[0].weight, 22.5)  # Weight after a successful workout
        self.assertEqual(workout.exercises[0].date_max_weight, date.today().strftime("%d/%m/%Y"))

if __name__ == '__main__':
    unittest.main()




