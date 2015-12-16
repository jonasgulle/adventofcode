#!/usr/bin/env python
import re

def main():
	ticker = {
		"children": [3, '='],
		"cats": [7, '='],
		"samoyeds": [2, '='],
		"pomeranians": [3, '='],
		"akitas": [0, '='],
		"vizslas": [0, '='],
		"goldfish": [5, '='],
		"trees": [3, '='],
		"cars": [2, '='],
		"perfumes": [1, '=']
	}

	with open("input") as f:
		data = map(lambda x: re.findall("\w+", x), map(lambda x: x.strip(), f.readlines()))

	sues = {}
	for sue in data:
		sues[sue[0]+" "+sue[1]] = { sue[2]: int(sue[3]), sue[4]: int(sue[5]), sue[6]: int(sue[7]) }

	for i in range(2):
		for sue, things in sues.iteritems():
			matches = 0
			for k, v in things.iteritems():
				if   ticker[k][1] == '<': matches += 1 if v < ticker[k][0] else 0
				elif ticker[k][1] == '>': matches += 1 if v > ticker[k][0] else 0
				elif ticker[k][1] == '=': matches += 1 if v == ticker[k][0] else 0

			if matches == 3:
				print "Part %d: It is %s!" % (i+1, sue)
				break

		# Oh, cats and trees should be greater than!
		ticker["cats"][1] = '>'
		ticker["trees"][1] = '>'
		# And pomeranians and goldfish less than!
		ticker["pomeranians"][1] = '<'
		ticker["goldfish"][1] = '<'


if __name__ == "__main__":
	exit(main())
