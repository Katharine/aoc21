# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

pos = (0, 0)
commands = {
	'forward': lambda pos, x: (pos[0] + x, pos[1]),
	'down': lambda pos, x: (pos[0], pos[1] + x),
	'up': lambda pos, x: (pos[0], pos[1] - x),
}
with open('day2.dat') as f:
	for line in f:
		command, value = line.strip().split()
		pos = commands[command](pos, int(value))
	print(pos[0] * pos[1])