#!/usr/bin/env python3

import sys
import re


ip_counts = {}


pattern = re.compile(
    r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
)

for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    match = pattern.match(line)

    if not match:
        continue

    ip = match.group(0)

   
    ip_counts[ip] = ip_counts.get(ip, 0) + 1



for ip in sorted(ip_counts):

    print(f"{ip}\t{ip_counts[ip]}")