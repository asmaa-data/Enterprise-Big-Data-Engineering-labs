#!/usr/bin/env python3

import sys
from collections import defaultdict

city_data = defaultdict(lambda: [0.0, 0.0, 0])

for line in sys.stdin:

    try:
        line = line.strip()

        if not line:
            continue

        parts = line.split("***")

        if len(parts) != 4:
            continue

        score = float(parts[0])
        city = parts[1]

        city_data[city][0] += score
        city_data[city][1] += score * score
        city_data[city][2] += 1

    except:

        continue


for city, (s, s2, c) in city_data.items():

    print(f"{city}\t{s}\t{s2}\t{c}")