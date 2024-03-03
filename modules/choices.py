import random

list = [20, 16, 10, 5]

print(random.choices(list,weights=(0.1,0.3,0.6,0.0),k=3))