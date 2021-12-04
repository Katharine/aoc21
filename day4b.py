# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def is_won(board, numbers):
    for i in range(5):
        did_win = True
        for j in range(5):
            if board[i][j] not in numbers:
                did_win = False
                break
        if did_win:
            return True

    for j in range(5):
        did_win = True
        for i in range(5):
            if board[i][j] not in numbers:
                did_win = False
                break
        if did_win:
            return True

def calc_score(board, numbers):
    result = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] not in numbers:
                result += board[i][j]
    return result * numbers[-1]

with open('day4.dat') as f:
    numbers = list(map(int, f.readline().strip().split(',')))

    boards = []
    print('hi')
    for line in f:
        if line.strip() == "":
            boards.append([])
            continue
        boards[-1].append(list(map(int, line.strip().split())))

    if len(boards[-1]) == 0:
        boards.pop()

used_numbers = []
used_indexes = set()
for number in numbers:
    used_numbers.append(number)
    for i, board in enumerate(boards):
        if i in used_indexes:
            continue
        if is_won(board, used_numbers):
            used_indexes.add(i)
            print("board won!")
            print(board)
            print(calc_score(board, used_numbers))