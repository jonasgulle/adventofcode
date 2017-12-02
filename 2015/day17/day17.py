#!/usr/bin/env python
from itertools import combinations

def main():
	with open("input") as f:
		containers = sorted([int(c) for c in f.readlines()])

	total = 0
	for i in range(4, len(containers)):
		for combo in combinations(containers, i):
			total += 1 if sum(combo) == 150 else 0

	print "Part 1: There are %d different combinations." % total

	total = 0
	for i in range(1, len(containers)):
		total = len([combo for combo in combinations(containers, i) if sum(combo) == 150])
		if total > 0:
			break

	print "Part 2: There are %d different ways using minimum number of containers." % total

if __name__ == "__main__":
	exit(main())
