#!/usr/bin/env python
# Day 2: http://adventofcode.com/

def part1(dims):
	def area(w, h, l):
		sides = (2*l*w, 2*w*h, 2*h*l)
		return sum(sides) + min(sides)/2

	print "The elves need %d square feet of paper." % (sum([area(d[0], d[1], d[2]) for d in dims]))

def part2(dims):
	from operator import mul

	def wrap(d):
		d.remove(max(d))
		return sum([i*2 for i in d])

	def bow(d):
		return reduce(mul, d, 1)

	print "The elves need %d square feet of ribbon." % sum([bow(d)+ wrap(d) for d in dims])

def main():
	with open("input") as f:
		dims = [map(int, d) for d in map(lambda x: map(lambda y: y.strip(), x.split('x')), f.readlines())]

	part1(dims)
	part2(dims)

	return 0

if __name__ == "__main__":
	exit(main())
