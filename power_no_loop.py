def power_x_by_y(x: int, y: int) -> int:
    return x if y == 1 else x * power_x_by_y(x, y-1)


print(power_x_by_y(4, 4))