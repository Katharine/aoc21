# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0


import collections

def diff(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


class Scanner:
    def __init__(self, points: set[tuple[int, int, int]]):
        self.points = points
        self.vectors = self._vectors()
        self.adjustments: list[tuple[tuple, tuple, tuple]] = []


    def _vectors(self):
        v = set()
        for a in self.points:
            for b in self.points:
                if a != b:
                    v.add(diff(a, b))
        return v


def permute(points: set[tuple[int,int,int]], permutation: tuple[int,int,int], flips: tuple[int,int,int]) -> set[tuple[int,int,int]]:
    p2 = set()
    for p in points:
        p2.add((p[permutation[0]] * flips[0], p[permutation[1]] * flips[1], p[permutation[2]] * flips[2]))
    return p2

def shift(points: set[tuple[int, int, int]], offset: tuple[int, int, int]):
    p2 = set()
    for p in points:
        p2.add((p[0] + offset[0], p[1] + offset[1], p[2] + offset[2]))
    return p2

with open('day19.dat') as f:
    scanners = []
    scanner_points = None
    for line in f:
        if line.startswith("---"):
            if scanner_points is not None:
                scanners.append(Scanner(scanner_points))
            scanner_points = set()
        elif line.strip() != "":
            scanner_points.add(tuple(map(int, line.strip().split(","))))
    scanners.append(Scanner(scanner_points))

Pair = collections.namedtuple('Pair', ('a', 'b', 'permute', 'flip', 'offset'))
pairs: list[Pair] = []
pair_map: dict[int, list[Pair]] = {}

permutations = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
sign_flips = [(+1, +1, +1), (+1, +1, -1), (+1, -1, -1), (-1, +1, +1), (-1, -1, +1), (-1, -1, -1), (+1, -1, +1), (-1, +1, -1)]

for i, scanner_a in enumerate(scanners):
    for j, scanner_b in enumerate(scanners):
        if i == j:
            continue
        for perm in permutations:
            for flip in sign_flips:
                v2 = permute(scanner_b.vectors, perm, flip)
                intersections = v2 & scanner_a.vectors
                if len(intersections) >= 132:
                    p2 = permute(scanner_b.points, perm, flip)
                    offset = None
                    overlapping_points = 0
                    for pa in scanner_a.points:
                        for pb in p2:
                            d = diff(pa, pb)
                            shifted_p2 = shift(p2, d)
                            if len(shifted_p2 & scanner_a.points) >= 12:
                                offset = d
                                overlapping_points = len(shifted_p2 & scanner_a.points)
                                break
                        else:
                            continue
                        break
                    if offset is None:
                        continue

                    print(f"Found pair ({len(intersections)}, {overlapping_points})! ({i}, {j}, {perm}, {flip}, {offset})")
                    pairs.append(Pair(j, i, perm, flip, offset))
                    pair_map.setdefault(j, []).append(pairs[-1])
                    break
            else:
                continue
            break

reoriented_scanners = {}
scanner_positions = {}

scanner_queue: list[tuple[int, int, list[int], Scanner]] = [(x, x, [], Scanner({(0, 0, 0)})) for x in range(len(scanners))]
while len(reoriented_scanners) != len(scanners):
    current_state, original_number, steps, scanner = scanner_queue.pop(0)
    if current_state == 0:
        if original_number not in reoriented_scanners:
            print(f"got {original_number}; {len(scanners) - len(reoriented_scanners)} to go")
            reoriented_scanners[original_number] = scanner
        continue
    for pair in pair_map[current_state]:
        if pair.b in steps:
            continue
        scanner_queue.append((pair.b, original_number, steps + [pair.b], Scanner(shift(permute(scanner.points, pair.permute, pair.flip), pair.offset))))


positions = []
for i, scanner in reoriented_scanners.items():
    positions.append(scanner.points.pop())

biggest_distance = 0
for a in positions:
    for b in positions:
        d = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        if d > biggest_distance:
            biggest_distance = d

print(f"biggest: {biggest_distance}")
