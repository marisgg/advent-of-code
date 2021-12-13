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
        if wins[c]:
            continue
        if np.any(np.all(board, axis=0)):
            # print(marks[c], c, 'column')
            column = boards[c][:, np.argmax(np.all(board, axis=0))]
            # print(boards[c], column)
            return np.sum(boards[c][np.where(~marks[c])]), c
        if np.any(np.all(board, axis=1)):
            # print(marks[c], c, 'row')
            row = boards[c][np.argmax(np.all(board, axis=0)), :]
            # print(boards[c], row)
            return np.sum(boards[c][np.where(~marks[c])]), c
    return None, None

win = np.zeros(shapes[0], dtype=bool)
last = None
for number in numbers:
    marks[np.where(boards == number)] = True
    c = 0
    while(c is not None):
        check, c = check_bingo(marks, boards, win)
        if c is not None and check is not None:
            print("Found bingo!")
            last = c
            win[c] = True
            print(check, c)
            print(number * check)
print(f'LAST: {last}')
