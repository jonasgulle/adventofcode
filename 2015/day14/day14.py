#!/usr/bin/env python
from operator import itemgetter

class Competition(object):
	def __init__(self, reindeers):
		self.reindeers = {}
		for name, speed, stamina, rest in reindeers:
			self.reindeers[name] = {
				"speed": speed,
				"stamina": stamina,
				"rest": rest,
				"dist": 0,
				"resting": 0,
				"flying": stamina,
				"points": 0
			}

	# Simulate one second
	def tick(self):
		for name in self.reindeers.keys():
			reindeer = self.reindeers[name]
			if reindeer["flying"] > 0:
				reindeer["dist"] += reindeer["speed"]
				reindeer["flying"] -= 1
			else:
				reindeer["resting"] += 1

			if reindeer["resting"] == reindeer["rest"]:
				reindeer["resting"] = 0
				reindeer["flying"] = reindeer["stamina"]
		self.give_points()

	def give_points(self):
		leaders = sorted(self.reindeers.iteritems(), key=itemgetter(1), reverse=True)
		best_dist = leaders[0][1]["dist"]
		for reindeer in leaders:
			if reindeer[1]["dist"] < best_dist:
				break
			self.reindeers[reindeer[0]]["points"] += 1

	def race(self, time):
		for i in range(time):
			self.tick()

	def best_dist(self):
		winner = sorted(self.reindeers.iteritems(), key=lambda k: k[1]["dist"], reverse=True)[0]
		return winner[0], winner[1]["dist"]

	def best_points(self):
		winner = sorted(self.reindeers.iteritems(), key=lambda k: k[1]["points"], reverse=True)[0]
		return winner[0], winner[1]["points"]

def main():
	with open("input") as f:
		reindeers = [x.strip().split(" ") for x in f.readlines()]

	# Extract name, speed, stamina and rest
	reindeers = [[d[0], int(d[3]), int(d[6]), int(d[-2])] for d in reindeers]

	competition = Competition(reindeers)
	competition.race(2503)
	reindeer, dist = competition.best_dist()
	print "Part 1: The winner is %s that travelled %d km." % (reindeer, dist)
	reindeer, points = competition.best_points()
	print "Part 2: The winner is %s that got %d points." % (reindeer, points)

	return 0

if __name__ == "__main__":
	exit(main())
