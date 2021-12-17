# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

x_min = 144
x_max = 178
y_min = -100
y_max = -76

vx = 0
vy = 0
x = 0
y = 0


def find_magic():
    workable = set()
    for vx_0 in range(179):
        for vy_0 in range(-101, 100):
            vy = vy_0
            vx = vx_0
            x = 0
            y = 0
            while True:
                y += vy
                vy -= 1
                x += vx
                if vx != 0:
                    if vx > 0:
                        vx -= 1
                    else:
                        vx += 1
                if y_min <= y <= y_max and x_min <= x <= x_max:
                    workable.add((vx_0, vy_0))
                    print(f"{vx_0},{vy_0} at {x},{y}")
                if y < y_min or x > x_max:
                    break
    return workable


print(len(find_magic()))
