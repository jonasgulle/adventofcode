#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations

class Happiness(object):
	def __init__(self, filename):
		with open(filename) as f:
			data = map(lambda x: x.strip().split(" "), f.readlines())
		self.data = [(d[0], int(d[3]) if d[2] == "gain" else -int(d[3]), d[-1][:-1]) for d in data]
		self.guests = defaultdict(dict)
		for name, happiness, opponent in self.data:
			self.guests[name][opponent] = happiness

	def calculate_happiness(self, seating):
		total = 0
		for i in range(len(seating) - 1):
			a, b = seating[i], seating[i+1]
			total += self.guests[a][b]
			total += self.guests[b][a]
		# And close the circle
		total += self.guests[seating[0]][seating[-1]]
		total += self.guests[seating[-1]][seating[0]]
		return total

	def add_apatethic_guest(self, name):
		for n in self.guests.keys():
			self.guests["Me"][n] = 0
			self.guests[n]["Me"] = 0

	def arrange_max_happiness(self):
		max_happiness = (0, None)
		for p in permutations(self.guests.keys()):
			h = self.calculate_happiness(p)
			if h > max_happiness[0]:
				max_happiness = (h, p)
		return max_happiness

def main():

	h = Happiness("input")
	happiness, seating = h.arrange_max_happiness()
	print "Part 1: The best seating is %s with %1d happiness." % (", ".join(seating), happiness)

	h.add_apatethic_guest("Me")
	happiness, seating = h.arrange_max_happiness()
	print "Part 2: The best seating is %s with %1d happiness." % (", ".join(seating), happiness)

	return 0

if __name__ == "__main__":
	exit(main())
