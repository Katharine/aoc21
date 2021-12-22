# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import re
from collections import namedtuple

rules = []
Rule = namedtuple('Rule', ('on', 'x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max'))
with open('day22.dat') as f:
    for line in f:
        g = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)..(-?\d+)", line)
        if not g:
            print(line)
            raise Exception("???")
        rules.append(Rule(g.group(1) == 'on', int(g.group(2)), int(g.group(3)), int(g.group(4)), int(g.group(5)), int(g.group(6)), int(g.group(7))))


def intersection_cuboid(a: Rule, b: Rule):
    if a.x_max < b.x_min or a.y_max < b.y_min or a.z_max < b.z_min or a.x_min > b.x_max or a.y_min > b.y_max or a.z_min > b.z_max:
        return None
    x = (min(a.x_max, b.x_max), max(a.x_min, b.x_min))
    y = (min(a.y_max, b.y_max), max(a.y_min, b.y_min))
    z = (min(a.z_max, b.z_max), max(a.z_min, b.z_min))
    return x[::-1], y[::-1], z[::-1]


def volume(c: Rule):
    return (c.x_max - c.x_min + 1) * (c.y_max - c.y_min + 1) * (c.z_max - c.z_min + 1)


done: list[Rule] = []
for rule in rules:
    real_off_rules = []
    print(f"------ {rule}")
    for s in done:
        i = intersection_cuboid(s, rule)
        if i is None:
            continue
        if s.on:
            print(f"Adding off cuboid {i}")
            real_off_rules.append(Rule(False, i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1]))
        else:
            print(f"Adding on cuboid {i} to counter a previous off cuboid we must have added")
            real_off_rules.append(Rule(True, i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1]))
    done.extend(real_off_rules)
    if rule.on:
        print(f"Adding on cuboid {rule[1:]}")
        done.append(rule)

total = 0
for d in done:
    if d.on:
        total += volume(d)
    else:
        total -= volume(d)
print(total)
