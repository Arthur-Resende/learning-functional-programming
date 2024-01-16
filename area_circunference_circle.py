from math import pi


def squared(x: int) -> float:
    return x * x


def get_area(diameter: int) -> float:
    RADIUS = diameter / 2
    return pi * squared(RADIUS)


def get_circumference(diameter: int) -> float:
    return diameter * pi


diameter = 5

print(f"the diameter is: {diameter}")
print(f"the area is: {get_area(diameter=diameter)}")
print(f"the circumference is: {get_circumference(diameter=diameter)}")