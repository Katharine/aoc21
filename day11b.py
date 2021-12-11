# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

octopodes = []
flash_count = 0
with open('day11.dat') as f:
    for line in f:
        octopodes.append(list(map(int, list(line.strip()))))


def incr_all():
    for x in range(len(octopodes[0])):
        for y in range(len(octopodes)):
            octopodes[x][y] += 1


def do_flashes():
    f = set()
    for x in range(len(octopodes[0])):
        for y in range(len(octopodes)):
            flash_octopus(x, y, f)
    for (x, y) in f:
        octopodes[x][y] = 0
    return len(f)


def incr_octopus(x, y, already_flashed):
    if (x, y) in already_flashed:
        return
    if x < 0 or y < 0 or x >= len(octopodes[0]) or y >= len(octopodes):
        return
    octopodes[x][y] += 1
    flash_octopus(x, y, already_flashed)


def flash_octopus(x, y, already_flashed):
    if (x, y) in already_flashed:
        return
    if octopodes[x][y] <= 9:
        return
    octopodes[x][y] = 0
    global flash_count
    flash_count += 1
    already_flashed.add((x, y))
    incr_octopus(x-1, y-1, already_flashed)
    incr_octopus(x-1, y, already_flashed)
    incr_octopus(x-1, y+1, already_flashed)
    incr_octopus(x, y-1, already_flashed)
    incr_octopus(x, y+1, already_flashed)
    incr_octopus(x+1, y-1, already_flashed)
    incr_octopus(x+1, y, already_flashed)
    incr_octopus(x+1, y+1, already_flashed)


x = 0
while True:
    x += 1
    incr_all()
    if do_flashes() == 100:
        print(x)
        break
for l in octopodes:
    print(' '.join(map(str, l)))
