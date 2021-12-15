# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import collections

with open('day15.dat') as f:
    world = []
    for line in f:
        world.append(list(map(int, line.strip())))

Entry = collections.namedtuple('Entry', ('risk', 'route'))
queue = [Entry(0, [(0, 0)])]
goal = (len(world[0]) - 1, len(world) - 1)
routes = []
visited: dict[tuple[int, int], int] = {}
work = 0
while queue:
    e = queue.pop(0)
    if e.route[-1] == goal:
        routes.append(e)
        continue
    if e.route[-1] in visited and e.risk > visited[e.route[-1]]:
        continue
    for p in [(1, 0), (0, 1)]:
        t = (e.route[-1][0] + p[0], e.route[-1][1] + p[1])
        if t[0] >= len(world[0]) or t[1] >= len(world):
            continue
        cost = world[t[0]][t[1]]
        if t in visited:
            if e.risk + cost >= visited[t]:
                continue
        visited[t] = e.risk + cost
        queue.append(Entry(e.risk + cost, e.route + [t]))
        work += 1

print(work)
print(sorted(routes, key=lambda x: x.risk)[:2])
