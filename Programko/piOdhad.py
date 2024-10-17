import random
import math

NUM = 100_000

inside = 0

for _ in range(0, NUM):
    if math.sqrt(random.uniform(0, 1)**2 + random.uniform(0, 1)**2) <= 1:
        inside += 1

print(4*(inside/NUM))
    
