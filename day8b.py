# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

# 0: 6
# 1: 2 easy
# 2: 5
# 3: 5
# 4: 4 easy
# 5: 5
# 6: 6
# 7: 3 easy
# 8: 7 easy
# 9: 6


with open('day8.dat') as f:
    counts = {1: 0, 4: 0, 7: 0, 8: 0}
    mapping = {4: 4, 2: 1, 3: 7, 7: 8}
    total = 0
    for line in f:
        line_mapping: dict[int, set] = {}
        a, b = line.split('|')
        groups = list(map(set, a.strip().split()))
        for group in groups:
            l = len(group)
            if l in mapping:
                line_mapping[mapping[l]] = group

        # known:
        # a, g, [cf], [bd]

        real_a = (line_mapping[7] - line_mapping[1]).pop()
        assert(len(line_mapping[7] - line_mapping[1]) == 1)
        # find nine
        for g in groups:
            if len(g) == 6 and len(g - set(real_a) - line_mapping[4]) == 1:
                nine = g
                assert(9 not in line_mapping)
                line_mapping[9] = nine
                real_g = (g - set(real_a) - line_mapping[4]).pop()
        # known: a, g
        # known: 1, 4, 8, 9
        # find zero
        for g in groups:
            if len(g) == 6 and len(g - line_mapping[9]) == 1 and len(line_mapping[1] & g) == 2:
                print(g)
                assert 0 not in line_mapping
                line_mapping[0] = g
                real_e = (g - line_mapping[9]).pop()

        # known:
        # a, g, e, c, f, [bd]
        # 0, 1, 2, 4, 8, 9
        print(line_mapping)
        for g in groups:
            if len(g) == 5 and real_e in g:
                assert 2 not in line_mapping
                line_mapping[2] = g
                print(g)
                print(line_mapping[1])
                real_f = (line_mapping[1] - g).pop()
                assert(len(line_mapping[1] - g) == 1)
                real_c = (line_mapping[1] - set(real_f)).pop()
                assert(len(line_mapping[1] - set(real_f)) == 1)
                real_b = (line_mapping[4] - line_mapping[2] - set(real_f)).pop()
                assert(len(line_mapping[4] - line_mapping[2] - set(real_f)) == 1)
                real_d = (set('abcdefg') - {real_a, real_b, real_c, real_e, real_f, real_g}).pop()
                assert(len(set('abcdefg') - {real_a, real_b, real_c, real_e, real_f, real_g}) == 1)

        import pprint
        pprint.pprint(groups)
        for g in groups:
            #print(g, {real_a, real_c, real_d, real_f, real_g})
            if g == {real_a, real_c, real_d, real_f, real_g}:
                line_mapping[3] = g
            elif g == {real_a, real_b, real_d, real_f, real_g}:
                line_mapping[5] = g
            elif g == {real_a, real_b, real_d, real_e, real_f, real_g}:
                line_mapping[6] = g
        print(f"a: {real_a}, b: {real_b}, c: {real_c}, d: {real_d}, e: {real_e}, f: {real_f}, g: {real_g}")
        pprint.pprint(line_mapping)
        assert(len(line_mapping) == 10)

        result_groups = list(map(set, b.strip().split()))
        digits = ''
        inverse_mapping = {}
        for i, v in line_mapping.items():
            inverse_mapping[frozenset(v)] = str(i)
        for g in result_groups:
            try:
                digits += inverse_mapping[frozenset(g)]
            except KeyError:
                print("Sometihng went wrong!")
                print(g)
                raise
        result = int(digits)
        print(result)
        total += result
    print(total)