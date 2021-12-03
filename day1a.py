# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day1.dat') as f:
	count = 0
	previous = None
	for line in f:
		n = int(line.strip())
		if previous is not None and n > previous:
			count += 1
		previous = n
	print(count)