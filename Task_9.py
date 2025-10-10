import random

random_number = [random.randint(-10, 10) for _ in range(15)]
print(random_number)

random_number_pos = [num for num in random_number if num > 0]
print(random_number_pos)

random_number_sq = [num ** 2 for num in random_number ]
print(random_number_sq)