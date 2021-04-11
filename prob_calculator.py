import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for n in range(value):
                self.contents.append(key)

    def draw(self, amount_balls):
        if amount_balls > len(self.contents):
            return self.contents
        else:
            random_balls = random.sample(self.contents, amount_balls)
            for ball in random_balls:
                self.contents.remove(ball)
            return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    for key, value in expected_balls.items():
        for n in range(value):
            expected.append(key)
    # The experiment
    counter = 0
    for n in range(num_experiments):
        balls_inside = copy.deepcopy(hat)
        random_balls = balls_inside.draw(num_balls_drawn)
        is_in = True
        for ball in expected:
            if ball in random_balls:
                random_balls.remove(ball)
            else:
                is_in = False
        if is_in == True:
            counter += 1

    probability = round(counter / num_experiments, 3)
    return probability
