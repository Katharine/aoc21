# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import string

paths: list[tuple[str, str]] = []
with open('day12.dat') as f:
    for line in f:
        paths.append(tuple(line.strip().split('-')))

connections = {}

for path in paths:
    if path[0] not in connections:
        connections[path[0]] = set()
    connections[path[0]].add(path[1])
    if path[1] not in connections:
        connections[path[1]] = set()
    connections[path[1]].add(path[0])

routes = []
queue: list[tuple[bool, list[str]]] = [(False, ['start', x]) for x in connections['start']]

while queue:
    route = queue.pop(0)
    if route[1][-1] == 'end':
        routes.append(route[1])
        continue
    else:
        cs = connections[route[1][-1]]
        for c in cs:
            if c != 'start' and (c[0] in string.ascii_uppercase or c not in route[1] or not route[0]):
                queue.append(((c[0] in string.ascii_lowercase and c in route[1]) or route[0], route[1] + [c]))

print(len(routes))
