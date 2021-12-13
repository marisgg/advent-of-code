import numpy as np

with open("inputs/3", "r") as file:
    input = file.read().splitlines()
    input = np.array([[int(y) for y in x] for x in input if x])

sums = np.sum(input, axis=0)

epsilon = ""
gamma = ""

for s in sums:
    if s > input.shape[0] / 2:
        # most common bit is 1
        epsilon += "1"
        gamma += "0"
    else:
        epsilon += "0"
        gamma += "1"

print(int(epsilon, 2) * int(gamma, 2), epsilon, gamma)
