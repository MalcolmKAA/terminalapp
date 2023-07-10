import unittest
from classes import Exercise, Workout

class TestWeightliftingApp(unittest.TestCase):

    def test_create_exercise(self):
        exercise = Exercise("Bench Press", 5, 5, 20.0, 60, 2.5)
        self.assertEqual(exercise.name, "Bench Press")
        self.assertEqual(exercise.sets, 5)
        self.assertEqual(exercise.reps, 5)
        self.assertEqual(exercise.weight, 20.0)
        self.assertEqual(exercise.rest_time, 60)
        self.assertEqual(exercise.weight_increase, 2.5)

    def test_create_and_execute_workout(self):
        exercise = Exercise("Bench Press", 5, 5, 20.0, 60, 2.5)
        workout = Workout("Workout A", [exercise])
        self.assertEqual(workout.name, "Workout A")
        self.assertEqual(workout.exercises[0], exercise)
if __name__ == '__main__':
    unittest.main()
