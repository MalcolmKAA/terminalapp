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