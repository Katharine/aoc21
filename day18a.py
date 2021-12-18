# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import json
import string

with open('day18.dat') as f:
    numbers = []
    for line in f:
        line = line.strip()
        number = []
        for c in line:
            if c in string.digits and number[-1][-1] in string.digits:
                number[-1] += c
            else:
                number.append(c)
        for i in range(len(number)):
            if number[i] not in ('[', ']', ','):
                number[i] = int(number[i])
        numbers.append(number)


def explode(number):
    depth = 0
    a = None
    b = None
    last_digit_pos = None
    add_to_next = None
    exploding = False
    pair_start = None
    pair_end = None
    to_remove = None
    for i, n in enumerate(number):
        if n == '[':
            pair_start = i
            pair_end = None
            depth += 1
            if depth > 4:
                exploding = True
            a = None
            b = None
        elif n == ']':
            pair_end = i
            if exploding and to_remove is None:
                to_remove = (pair_start, pair_end)
            depth -= 1
        elif n != ',':
            if add_to_next is not None:
                number[i] += add_to_next
                break
            if not exploding:
                last_digit_pos = i
            if a is None:
                a = n
            elif b is None:
                b = n
                if exploding:
                    if last_digit_pos is not None:
                        number[last_digit_pos] += a
                    add_to_next = b
    if exploding:
        number[to_remove[0]:to_remove[1]+1] = [0]
    return exploding


def split(number):
    for i, n in enumerate(number):
        if isinstance(n, int) and n > 9:
            number[i:i+1] = ['[', n // 2, ',', (n // 2) + (n % 2), ']']
            return True
    return False


def add(a, b):
    return ['['] + a + [','] + b + [']']


def treeify(n):
    return json.loads(''.join(map(str, n)))


def magnitude(n):
    if isinstance(n, int):
        return n
    if len(n) != 2:
        raise Exception("???")
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


number = numbers.pop(0)
for b in numbers:
    number = add(number, b)
    while True:
        exploded = explode(number)
        if not exploded:
            s = split(number)
            if not s:
                break

print(''.join(map(str, number)))
print(magnitude(treeify(number)))
