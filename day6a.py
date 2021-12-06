# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('b') as f:
    fish = list(map(int, f.readline().split(',')))

for i in range(256):
    new_fish = []
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            new_fish.append(8)
        else:
            fish[i] = f - 1

    fish.extend(new_fish)

print(len(fish))
