from itertools import combinations
import math
from collections import Counter
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents += [ball] * count

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents.copy()
        balls_drawn = []
        for i in range(num_balls):
            ball = random.choice(self.contents)
            balls_drawn.append(ball)
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    total_combinations = math.comb(len(hat.contents), num_balls_drawn)
    expected_combinations = 0
    for comb in combinations(hat.contents, num_balls_drawn):
        count = Counter(comb)
        success = True
        for ball, expected_count in expected_balls.items():
            if count[ball] < expected_count:
                success = False
                break
        if success:
            expected_combinations += 1
    probability = expected_combinations / total_combinations
    return probability
hat = Hat(blue=5, red=4, green=2)
expected_balls = {"red": 1, "green": 2}
num_balls_drawn = 4
num_experiments = 1

probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(f"The probability of drawing {num_balls_drawn} balls from the hat and getting at least {expected_balls} is {probability:.3f}")
