import numpy as np

with open("inputs/2", "r") as file:
    input = file.read().splitlines()
    input = [x for x in input if x]
depth = 0
horizontal = 0
for line in input:
    direction, value = line.split(" ")
    value = int(value)
    print(direction, value)
    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value
    else:
        Exception("Direction not supported or formatted properly.")
        break
print(f'depth * horizontal = {depth} * {horizontal} = {depth * horizontal}')