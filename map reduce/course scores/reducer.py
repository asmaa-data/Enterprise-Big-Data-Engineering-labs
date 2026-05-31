#!/usr/bin/env python3

import sys
import math
from collections import defaultdict

data = defaultdict(lambda: [0.0, 0.0, 0])

for line in sys.stdin:

    try:
        line = line.strip()

        if not line:
            continue

        city, s, s2, c = line.split("\t")

        data[city][0] += float(s)
        data[city][1] += float(s2)
        data[city][2] += int(c)

    except:
        continue


for city, (s, s2, c) in data.items():

    if c == 0:
        continue

    mean = s / c
    variance = (s2 / c) - (mean * mean)

    if variance < 0:
        variance = 0

    std = math.sqrt(variance)

    print(f"{city}\tCOUNT={c}\tMEAN={mean:.2f}\tSTD={std:.2f}")