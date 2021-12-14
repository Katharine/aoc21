# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day14.dat') as f:
    template = f.readline().strip()
    f.readline()
    rules = {}
    for line in f:
        f, t = line.strip().split(' -> ')
        rules[f] = t

pairs = {}
for i in range(len(template) - 1):
    pairs[template[i:i+2]] = pairs.get(template[i:i+2], 0) + 1

for step in range(40):
    for pair, count in pairs.copy().items():
        if pair in rules:
            pair1 = pair[0] + rules[pair]
            pair2 = rules[pair] + pair[1]
            pairs[pair] -= count
            pairs[pair1] = pairs.get(pair1, 0) + count
            pairs[pair2] = pairs.get(pair2, 0) + count

# hack: this works iff the template starts and ends with the same letter (mine did)
frequencies = {template[0]: 2}
for pair, count in pairs.items():
    frequencies[pair[0]] = frequencies.get(pair[0], 0) + count
    frequencies[pair[1]] = frequencies.get(pair[1], 0) + count

max_c, max_v = max(((k, v) for k, v in frequencies.items()), key=lambda x: x[1])
min_c, min_v = min(((k, v) for k, v in frequencies.items()), key=lambda x: x[1])

print(max_c, min_c, max_v//2, min_v//2, max_v//2 - min_v//2)