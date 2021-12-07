# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day7.dat') as f:
    crabs = list(map(int, f.readline().split(',')))

max_option = max(crabs)
best_fuel = None
for p in range(max_option):
    f = 0
    for crab in crabs:
        t = abs(crab - p)
        f += t * (1 + t) // 2
    if best_fuel is None or f < best_fuel:
        best_fuel = f

print(best_fuel)
