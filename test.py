import unittest
from unittest.mock import patch
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
    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1'])
    def test_execute_workout_successful(self):
        exercise = Exercise("Bench Press", 5, 5, 50, 30, 5)
        workout = Workout("Workout A", [exercise])
        workout.execute_workout()
        self.assertEqual(exercise.current_set, 5)
        self.assertEqual(exercise.current_weight, 55)
        self.assertEqual(exercise.max_weight, 55)

if __name__ == '__main__':
    unittest.main()

