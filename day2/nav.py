#!/usr/bin/env python3

import sys

horiPos = 0
depth = 0
aim = 0

with open(sys.argv[1],'r') as fp:
    for line in fp:
        motion = line.split(' ')[0]
        distance = int(line.split(' ')[1])
        if motion == 'forward':
            horiPos += distance
            depth += distance*aim
        elif motion == 'up':
            aim -= distance
        elif motion == 'down':
            aim += distance
print("The sub has a horizontal position of ",horiPos)
print("and a depth of ",depth)
print("The product of these is ",(horiPos*depth))
