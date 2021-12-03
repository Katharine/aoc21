# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day3.dat') as f:
	lines = f.read().strip().split("\n")

bits = ''
for i in range(12):
	counter = 0
	for l in lines:
		counter += int(l[i])
	bits += str(int(counter > len(lines) // 2))

print(bits)
gamma = int(bits, 2)
epsilon = ~gamma & 0b111111111111
print(gamma * epsilon)