# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day8.dat') as f:
    counts = {1: 0, 4: 0, 7: 0, 8: 0}
    mapping = {4: 4, 2: 1, 3: 7, 7: 8}
    for line in f:
        a, b = line.split('|')
        groups = b.strip().split()
        for group in groups:
            l = len(group)
            if l in mapping:
                counts[mapping[l]] += 1

    print(sum(counts.values()))