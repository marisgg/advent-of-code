import numpy as np
import sys



with open(sys.argv[1], "r") as file:
    input = file.read().splitlines()
    numbers = np.array([int(x) for x in input[0].split(',')])
    input = input[2:]
    shapes = (3 if 'test' in sys.argv[1] else 100, 5, 5)
    boards = np.array([[int(number) for number in inputline.split(' ') if number] for inputline in input if inputline]).reshape(shapes)
    marks = np.zeros(shapes, dtype=bool)

# print(np.unique(boards))
# print(np.unique(numbers))

def check_bingo(marks, boards, wins):
    for c, board in enumerate(marks):
        if np.any(np.all(board, axis=0)):
            print(marks[c], c, 'column')
            column = boards[c][:, np.argmax(np.all(board, axis=0))]
            print(boards[c], column)
            return np.sum(boards[c][np.where(~marks[c])]), c
        if np.any(np.all(board, axis=1)):
            print(marks[c], c, 'row')
            row = boards[c][np.argmax(np.all(board, axis=0)), :]
            print(boards[c], row)
            return np.sum(boards[c][np.where(~marks[c])]), c
    return None, None

for number in numbers:
    marks[np.where(boards == number)] = True
    check, c = check_bingo(marks, boards)
    if check:
        print(number * check)
        break