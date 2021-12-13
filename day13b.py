# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

points = set()
folds: list[tuple[str, int]] = []
with open('day13.dat') as f:
    for line in f:
        if line.strip() == "":
            break
        points.add(tuple(map(int, line.strip().split(','))))
    for line in f:
        instr = line.strip().split()[2]
        axis, coord = instr.split("=")
        folds.append((axis, int(coord)))


def do_fold(points: set[tuple[int, int]], axis, coord):
    cm = {'x': 0, 'y': 1}
    axis = cm[axis]
    to_remove = []
    to_add = []
    for point in points:
        if point[axis] > coord:
            to_remove.append(point)
            p = list(point)
            p[axis] = coord - (p[axis] - coord)
            to_add.append(tuple(p))

    for i in to_remove:
        points.remove(i)

    for i in to_add:
        points.add(i)

for fold in folds:
    do_fold(points, *fold)

max_x = max(x[0] for x in points)
max_y = max(x[1] for x in points)

print(max_x, max_y)

for y in range(max_y+1):
    line = ''
    for x in range(max_x+1):
        if (x, y) in points:
            line += '#'
        else:
            line += ' '
    print(line)
