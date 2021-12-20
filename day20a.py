# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

image = []
with open('day20.dat') as f:
    algorithm = f.readline().strip()
    f.readline()
    for line in f:
        image.append(list(line.strip()))
        print(line.strip())


def enlarge(image, default='.'):
    new_len = len(image[0]) + 6
    new_image = [[default] * new_len] * 3
    for row in image:
        new_image.append([default] * 3 + row + [default] * 3)
    new_image.extend([[default] * new_len] * 3)
    return new_image


def idx(im, x, y, default='.'):
    if x < 0 or y < 0 or x >= len(im[0]) or y >= len(im):
        return default
    return im[y][x]


def nf(im, x, y, d='.'):
    parts = idx(im, x-1, y-1, d) + idx(im, x, y-1, d) + idx(im, x+1, y-1, d) + idx(im, x-1, y, d) + idx(im, x, y, d) + idx(im, x+1, y, d) + idx(im, x-1, y+1, d) + idx(im, x, y+1, d) + idx(im, x+1, y+1, d)
    return int(parts.replace('.', '0').replace('#', '1'), 2)


for i in range(2):
    d = ['.', '#'][i % 2]
    image = enlarge(image, default=d)
    new_image = []
    for y in range(len(image)):
        r = []
        for x in range(len(image[y])):
            r.append(algorithm[nf(image, x, y, d)])
        new_image.append(r)
    image = new_image


light_count = 0
for y in range(len(image)):
    for x in range(len(image[y])):
        if image[y][x] == '#':
            light_count += 1

print(light_count)
