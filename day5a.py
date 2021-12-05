# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

positions = {}

with open('day5.dat') as f:
    for line in f:
        a, b = line.strip().split(' -> ')
        ax, ay = map(int, a.split(','))
        bx, by = map(int, b.split(','))
        if ax == bx:
            if by < ay:
                ax, bx = bx, ax
                ay, by = by, ay
            y = ay
            while y <= by:
                positions[ax, y] = positions.get((ax, y), 0) + 1
                y += 1
        elif ay == by:
            if bx < ax:
                ax, bx = bx, ax
                ay, by = by, ay
            x = ax
            while x <= bx:
                positions[x, ay] = positions.get((x, ay), 0) + 1
                x += 1

counter = 0
for position in positions.values():
    if position >= 2:
        counter += 1

print(counter)