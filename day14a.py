# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day14.dat') as f:
    template = f.readline().strip()
    f.readline()
    rules = {}
    for line in f:
        f, t = line.strip().split(' -> ')
        rules[f] = t

output = template
for step in range(10):
    next_output = ''
    for i in range(len(output) - 1):
        next_output += output[i]
        insertion = rules.get(output[i:i+2])
        if insertion is not None:
            next_output += insertion
    next_output += output[-1]
    output = next_output

chr_counts = {}
for c in output:
    chr_counts[c] = chr_counts.get(c, 0) + 1

max_c, max_v = max(((k, v) for k, v in chr_counts.items()), key=lambda x: x[1])
min_c, min_v = min(((k, v) for k, v in chr_counts.items()), key=lambda x: x[1])

print(max_c, min_c, max_v, min_v, max_v - min_v)