# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

player_1_start = 7
player_2_start = 9

ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

import collections

GameState = collections.namedtuple('GameState', ('p1_pos', 'p1_score', 'p2_pos', 'p2_score', 'turn'))
games: dict[GameState, int] = collections.defaultdict(int)
won_games = [0, 0]
games[GameState(player_1_start, 0, player_2_start, 0, 0)] = 1

while len(games) != 0:
    for game, count in games.copy().items():
        for roll, roll_count in ROLLS.items():
            if game.turn == 0:
                new_pos = ((game.p1_pos + roll - 1) % 10) + 1
                new_score = game.p1_score + new_pos
                if new_score >= 21:
                    won_games[0] += count * roll_count
                else:
                    games[GameState(new_pos, new_score, game.p2_pos, game.p2_score, 1)] += count * roll_count
            elif game.turn == 1:
                new_pos = ((game.p2_pos + roll - 1) % 10) + 1
                new_score = game.p2_score + new_pos
                if new_score >= 21:
                    won_games[1] += count * roll_count
                else:
                    games[GameState(game.p1_pos, game.p1_score, new_pos, new_score, 0)] += count * roll_count

        del games[game]
    print(len(games))


print(f"won games: {won_games}")

