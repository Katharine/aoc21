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
    for vy_0 in range(1000):
        vy = vy_0
        x = 0
        y = 0
        y_peak = 0
        while True:
            y += vy
            vy -= 1
            if y > y_peak:
                y_peak = y
            if y_min <= y <= y_max:
                print(vy_0, y_peak)
                break
            if y < y_min or x > x_max:
                break


find_magic()
