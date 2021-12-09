# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

world = []
with open('day9.dat') as f:
    for line in f:
        world.append(list(map(int, list(line.strip()))))

risk = 0
for i in range(len(world[0])):
    for j in range(len(world)):
        is_low = (i == 0 or world[i][j] < world[i-1][j]) and (j == 0 or world[i][j] < world[i][j-1]) and (i == len(world[0])-1 or world[i][j] < world[i+1][j]) and (j == len(world)-1 or world[i][j] < world[i][j+1])
        if is_low:
            risk += 1 + world[i][j]

print(risk)
