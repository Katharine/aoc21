# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

player_1_start = 7
player_2_start = 9

class Player:
    def __init__(self, start):
        self.pos = start
        self.score = 0

players = [Player(7), Player(9)]

roll_count = 0
def roll_die():
    i = 1
    global roll_count
    while True:
        roll_count += 1
        yield i
        i = (i % 100) + 1

d = roll_die()
while True:
    for p in players:
        roll = next(d) + next(d) + next(d)
        print(roll)
        new_pos = ((p.pos + roll - 1) % 10) + 1
        p.pos = new_pos
        p.score += new_pos
        if p.score >= 1000:
            break
    else:
        continue
    break

print([x.score for x in players], roll_count)
print(min(x.score for x in players) * roll_count)