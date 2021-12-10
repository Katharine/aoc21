# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def score(line):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    stack = []
    mapping = {'>': '<', ')': '(', '}': '{', ']': '['}
    score = 0
    for chr in line.strip():
        if chr in ('(', '[', '{', '<'):
            stack.append(chr)
        else:
            if len(stack) > 0 and stack[-1] == mapping[chr]:
                stack.pop()
            elif len(stack) > 0:
                return 0
    for remaining in stack[::-1]:
        score = score * 5 + scores[remaining]
    return score

with open('day10.dat') as f:
    scores = [score(l) for l in f if score(l) != 0]
    print(sorted(scores)[len(scores)//2])