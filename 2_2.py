import numpy as np

with open("inputs/2", "r") as file:
    input = file.read().splitlines()
    input = [x for x in input if x]
depth = 0
horizontal = 0
aim = 0
for line in input:
    direction, value = line.split(" ")
    value = int(value)
    print(direction, value)
    if direction == "forward":
        horizontal += value
        depth += aim * value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value
    else:
        Exception("Direction not supported or formatted properly.")
        break
print(f'depth * horizontal = {depth} * {horizontal} = {depth * horizontal}')