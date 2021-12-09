# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

world = []
with open('day9.dat') as f:
    for line in f:
        world.append(list(map(int, list(line.strip()))))

low_points = []
for i in range(len(world[0])):
    for j in range(len(world)):
        is_low = (i == 0 or world[i][j] < world[i-1][j]) and (j == 0 or world[i][j] < world[i][j-1]) and (i == len(world[0])-1 or world[i][j] < world[i+1][j]) and (j == len(world)-1 or world[i][j] < world[i][j+1])
        if is_low:
            low_points.append((i, j))

basins = []
for point in low_points:
    # a basin requires expanding out from a low point in every direction we can keep incrementing
    basin_points = set()
    point_queue = [point]
    while point_queue:
        i, j = point_queue.pop(0)
        if i < 0 or j < 0 or i >= len(world[0]) or j >= len(world):
            continue
        if world[i][j] == 9:
            continue
        if (i, j) in basin_points:
            continue
        point_queue.extend([(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
        basin_points.add((i, j))
    basins.append((frozenset(basin_points)))

top_basins = sorted(list(map(len, basins)))[::-1][:3]

print(top_basins[0] * top_basins[1] * top_basins[2])
