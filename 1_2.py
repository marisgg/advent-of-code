import numpy as np

count = 0

with open("inputs/1", "r") as file:
    input = file.read().splitlines()
    input = [int(x) for x in input if x]

sums = []

for idx, line in enumerate(input):
    summer = 0
    if idx+3 <= len(input):
        summer = np.sum(np.array(input[idx : idx+3]))
    sums.append(summer)
    greater = False
    if sums[idx] > sums[idx-1]:
        count += 1
        greater = True
    print(f"{idx}: {summer} : {greater}")
print(count)