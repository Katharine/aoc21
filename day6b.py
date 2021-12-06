# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day6.dat') as f:
    fish = list(map(int, f.readline().split(',')))


remaining_days = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for f in fish:
    remaining_days[f] += 1

for i in range(256):
    done = remaining_days.pop(0)
    remaining_days[6] += done
    remaining_days.append(done)

print(sum(remaining_days))
