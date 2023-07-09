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