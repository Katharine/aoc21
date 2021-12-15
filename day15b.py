# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import collections

with open('day15.dat') as f:
    world = []
    for line in f:
        world.append(list(map(int, line.strip())))


def munge_row(r):
    return [x % 9 + 1 for x in r]

l = len(world[0])
for row in world:
    for i in range(4):
        row.extend(munge_row(row[i*l:(i+1)*l]))
print(l, len(world[0]))

l = len(world)
for i in range(4):
    world.extend(munge_row(r) for r in world[i*l:(i+1)*l])

print(l, len(world))

Entry = collections.namedtuple('Entry', ('risk', 'route'))
queue = [Entry(0, [(0, 0)])]
goal = (len(world[0]) - 1, len(world) - 1)
routes = []
visited = {}
work = 0
while queue:
    e = queue.pop(0)
    if e.route[-1] == goal:
        routes.append(e)
        continue
    if e.route[-1] in visited and e.risk > visited[e.route[-1]]:
        continue
    for p in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        t = (e.route[-1][0] + p[0], e.route[-1][1] + p[1])
        if t[0] >= len(world[0]) or t[1] >= len(world) or t[0] < 0 or t[1] < 0:
            continue
        cost = world[t[0]][t[1]]
        if t in visited:
            if e.risk + cost >= visited[t]:
                continue
        if e.risk + cost > ((len(world[0])) + (len(world))) * 9:
            continue
        visited[t] = e.risk + cost
        queue.append(Entry(e.risk + cost, e.route + [t]))
        work += 1

print(work)
print(list(x.risk for x in sorted(routes, key=lambda x: x.risk)[:5]))
