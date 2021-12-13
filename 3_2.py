import numpy as np

with open("inputs/3", "r") as file:
    input = file.read().splitlines()
    input = np.array([[int(y) for y in x] for x in input if x])

sums = np.sum(input, axis=0)

def get_num(idx, data, mostcommon):
    if len(data) == 1:
        print(data)
        return "".join(str(x) for x in data.flat)
    s = np.sum(data, axis=0)[idx]
    if s > data.shape[0] / 2:
        # 1 is most common
        data = data[np.where(data[:,idx] == (1 if mostcommon else 0))]
    elif s == data.shape[0] / 2:
        # even common
        data = data[np.where(data[:,idx] == (1 if mostcommon else 0))]
    else:
        # 0 is most common
        data = data[np.where(data[:,idx] == (0 if mostcommon else 1))]
    return get_num(idx+1, data, mostcommon)

oxygen = get_num(0, input, False)
co2 = get_num(0, input, True)
print(oxygen, co2)
print(int(oxygen, 2), int(co2, 2))
print(int(oxygen, 2) * int(co2, 2))