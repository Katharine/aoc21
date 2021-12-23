ROOM_NAMES = ['A', 'B', 'C', 'D']
LETTER_ROOMS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
MOVE_COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOM_INDEXES = [2, 4, 6, 8]
ROOM_DEPTH = 4

import heapq

class World:
    def __init__(self, rooms):
        self.rooms = rooms
        self.waiting = ['', '', '', '', '', '', '', '', '', '', '']

    def copy(self):
        w = World(tuple(x[:] for x in self.rooms))
        w.waiting = self.waiting[:]
        return w

    def __hash__(self):
        return hash(self._as_tuple())

    def _as_tuple(self):
        return tuple(tuple(x) for x in self.rooms), tuple(self.waiting)

    def __eq__(self, other):
        return isinstance(other, World) and self._as_tuple() == other._as_tuple()


    def possible_worlds(self):
        possibilities = []
        # consider moving someone out of a waiting space into a room
        # this can only possibly be into the correct room
        for i, letter in enumerate(self.waiting):
            if letter == '':
                continue
            dest_room = LETTER_ROOMS[letter]
            dest_index = ROOM_INDEXES[dest_room]
            # can't move into a full room, or a room containing other letters
            if len(self.rooms[dest_room]) == ROOM_DEPTH or len(set(self.rooms[dest_room]) - set(letter)) > 0:
                continue
            direction = 1 if dest_index > i else -1
            for intervening_space in self.waiting[i + direction:dest_index:direction]:
                if intervening_space != '':
                    break
            else:
                # there's nothing in the way and the room is acceptable - this is a possible world
                w = self.copy()
                w.waiting[i] = ''
                w.rooms[LETTER_ROOMS[letter]].append(letter)
                cost = (abs(i - dest_index) + ROOM_DEPTH - len(w.rooms[dest_room]) + 1) * MOVE_COSTS[letter]
                possibilities.append((cost, w))
        # consider moving someone out of a room into a waiting space
        for i, room in enumerate(self.rooms):
            if len(room) == 0:
                continue
            letter = room[-1]
            # if in the correct room and don't need to move anyone out, leaving is not an option
            if letter == ROOM_NAMES[i] and len(set(room[:-1]) - set(ROOM_NAMES[i])) == 0:
                continue
            # consider all the waiting room options:
            for j in range(ROOM_INDEXES[i], -1, -1):
                try:
                    cost, world = self._check_waiting_space(letter, i, j)
                    if cost is not None:
                        possibilities.append((cost, world))
                except StopIteration:
                    break
            for j in range(ROOM_INDEXES[i], len(self.waiting)):
                try:
                    cost, world = self._check_waiting_space(letter, i, j)
                    if cost is not None:
                        possibilities.append((cost, world))
                except StopIteration:
                    break
        return possibilities

    def _check_waiting_space(self, letter, current, space):
        # can't stop outside a room
        if space in ROOM_INDEXES:
            return None, None
        if self.waiting[space] == '':
            w = self.copy()
            cost = (ROOM_DEPTH - len(w.rooms[current]) + abs(space - ROOM_INDEXES[current]) + 1) * MOVE_COSTS[letter]
            w.waiting[space] = w.rooms[current].pop()
            return cost, w
        raise StopIteration

    def __str__(self):
        sr = "#" * (len(self.waiting) + 2)
        sr += "\n#" + ''.join(x if x != '' else ' ' for x in self.waiting) + "#\n"
        for i in range(ROOM_DEPTH):
            sr += '  #' if i > 0 else '###'
            sr += '#'.join(x[ROOM_DEPTH - i - 1] if len(x) >= ROOM_DEPTH - i else ' ' for x in self.rooms)
            sr += '#  \n' if i > 0 else '###\n'
        sr += '  ##########'
        return sr

    def __lt__(self, other):
        return False


def is_target_world(world: World) -> bool:
    for i, room in enumerate(world.rooms):
        if len(room) != ROOM_DEPTH or len(set(room) - set(ROOM_NAMES[i])) != 0:
            return False
    return True

start_world = World((['C', 'D', 'D', 'D'], ['A', 'B', 'C', 'D'], ['B', 'A', 'B', 'B'], ['C', 'C', 'A', 'A']))

tried = set()
q = [(0, start_world, [(0, start_world)])]
heapq.heapify(q)
i = 0
while q:
    c, v, path = heapq.heappop(q)
    if v in tried:
        continue
    tried.add(v)
    if is_target_world(v):
        print("\n------\n".join(f"cost: {x[0]}\n{x[1]}" for x in path))
        print(c)
        break
    options = v.possible_worlds()
    print(c)
    for cost, world in options:
        heapq.heappush(q, (c + cost, world, path + [(cost, world)]))

