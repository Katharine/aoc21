# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def score(line):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    mapping = {'>': '<', ')': '(', '}': '{', ']': '['}
    for chr in line.strip():
        if chr in ('(', '[', '{', '<'):
            stack.append(chr)
        else:
            if len(stack) > 0 and stack[-1] == mapping[chr]:
                stack.pop()
            else:
                return scores[chr]
    return 0


with open('day10.dat') as f:
    print(sum(score(l) for l in f))