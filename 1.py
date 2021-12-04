count = 0

with open("inputs/1", "r") as file:
    input = file.read().splitlines()

for idx, line in enumerate(input):
    # print(f"{idx}: {line}")
    if idx == 0 or line == "":
        continue
    if int(line) > int(input[idx-1]):
        count += 1
print(count)