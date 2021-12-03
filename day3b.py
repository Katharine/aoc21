# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from __future__ import division

with open('day3.dat') as f:
	lines = f.read().strip().split("\n")

def do_thing(survivors, tie_breaker, comparator):
	survivors = survivors[:]
	for i in range(12):
		counter = 0
		for l in survivors:
			counter += int(l[i])
		most_common = str(int(comparator(counter, len(survivors) / 2)))
		if counter == len(survivors) / 2:
			most_common = str(tie_breaker)
		new_survivors = []
		for l in survivors:
			if l[i] == most_common:
				new_survivors.append(l)
		survivors = new_survivors
		if len(survivors) == 1:
			break
	if len(survivors) != 1:
		raise Exception("too many survivors!!!!")
	return survivors[0]


oxygen = do_thing(lines, 1, lambda a, b: a > b)
co2 = do_thing(lines, 0, lambda a, b: a < b)
print(oxygen, co2, int(oxygen, 2) * int(co2, 2))
