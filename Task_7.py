import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

for radius in range(5,9 + 1):
    print(calculate_circle_area(radius))
for number in range(-5,10 + 1):
    print(is_positive(number))