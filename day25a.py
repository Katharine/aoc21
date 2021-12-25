# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

world = {}
max_x = 0
max_y = 0
with open('day25.dat') as f:
    for y, line in enumerate(f):
        max_y += 1
        max_x = len(line.strip())
        for x, chr in enumerate(line.strip()):
            if chr in ('v', '>'):
                world[x, y] = chr


def run_step(world: dict[tuple[int, int]]):
    new_world = {}
    moves = 0
    for (x, y), direction in world.items():
        if direction == '>':
            new_x = x + 1
            if new_x >= max_x:
                new_x = 0
            if (new_x, y) not in world:
                moves += 1
                new_world[new_x, y] = direction
            else:
                new_world[x, y] = direction
        else:
            new_world[x, y] = direction
    world = new_world
    new_world = {}
    for (x, y), direction in world.items():
        if direction == 'v':
            new_y = y + 1
            if new_y >= max_y:
                new_y = 0
            if (x, new_y) not in world:
                moves += 1
                new_world[x, new_y] = direction
            else:
                new_world[x, y] = direction
        else:
            new_world[x, y] = direction
    return new_world, moves

i = 0
while True:
    i += 1
    world, moves = run_step(world)
    print(moves)
    if moves == 0:
        print(f"Finished on step {i}")
        break
