import random

NUM = 1_000_000

def generate_random_points():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    return x, y

def distance_squared(x, y):
    return x**2 + y**2

def is_in_circle(distance):
    return distance <= 1

def pi_estimate():
    inside = 0
    
    for _ in range(0, NUM):
        # nemusím odmocňovat vzdálenost, když je vzdalenost^2 < 1 tak i odmocnina bude < 1
        x, y = generate_random_points()
        if is_in_circle(distance_squared(x, y)):
            inside += 1

    return 4*(inside/NUM)

print(pi_estimate())
    
