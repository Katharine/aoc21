# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day1.dat') as f:
	count = 0
	n_2 = int(next(f).strip())
	n_1 = int(next(f).strip())
	previous = None
	for line in f:
		n = int(line.strip())
		s = n + n_1 + n_2
		n_2 = n_1
		n_1 = n
		if previous is not None and s > previous:
			count += 1
		previous = s
	print(count)