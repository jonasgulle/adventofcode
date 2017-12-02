#!/usr/bin/env python

# Naive solution with pure brute force.
# I bet there are other, more elegant, solutions to this problem :)

def read_locations(filename="input"):
	with open(filename) as f:
		data = [x.strip().split(" ") for x in f.readlines()]

	paths = {}
	cities = set(([d[0] for d in data] + [d[2] for d in data]))
	for city in cities:
		paths[city] = {}
		for dest in cities:
			if dest == city:
				continue
			for d in data:
				if d[0] == city and d[2] == dest:
					paths[city][dest] = int(d[-1])

	return paths

def bruteforce():
	from itertools import permutations
	paths = read_locations()

	shortest_dist, shortest_route = 1e9, None
	longest_dist, longest_route = 0, None
	for l in permutations(paths.keys()):
		route = 0
		for i in range(len(l)-1):
			src, dst = l[i], l[i+1]
			try:
				dist = paths[src][dst]
			except KeyError:
				dist = paths[dst][src]
			route += dist

		if route < shortest_dist:
			shortest_dist = route
			shortest_route = "->".join(l)

		if route > longest_dist:
			longest_dist = route
			longest_route = "->".join(l)

	return (shortest_dist, shortest_route), (longest_dist, longest_route)

def main():
	shortest, longest = bruteforce()
	print "Part 1: The shortest route is %d (%s)" % (shortest[0], shortest[1])
	print "Part 2: The longest route is %d (%s)" % (longest[0], longest[1])
	return 0

if __name__ == "__main__":
	exit(main())
