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

print(len(points))
do_fold(points, folds[0][0], folds[0][1])
print(len(points))
