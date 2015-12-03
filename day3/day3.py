#!/usr/bin/env python
# Day 2: http://adventofcode.com/

def advance(op, x, y):
	if   op == '<': x -= 1
	elif op == '>': x += 1
	elif op == '^': y -= 1
	elif op == 'v': y += 1
	else: raise Exception("Unknown direction")
	return x, y

def part1(route):
	# Memory is cheap
	length = 1024 # Arbitrary
	matrix = bytearray(pow(length, 2))

	# Start in the middle of the array
	x = length / 2
	y = x

	for op in route:
		matrix[y*length+x] += 1
		x, y = advance(op, x, y)
		matrix[y*length+x] += 1

	houses = 0
	for i in range(len(matrix)):
		if matrix[i] > 0:
			houses += 1

	print "Part 1: %d houses got at least one present." % houses

def part2(route):
	# Memory is cheap
	length = 1024 # Arbitrary
	matrix = bytearray(pow(length, 2))

	santa = [route[i] for i in range(0, len(route), 2)]
	robot = [route[i] for i in range(1, len(route), 2)]

	sx, rx = length / 2, length / 2
	sy, ry = sx, rx
	for sop, rop in zip(santa, robot):
		# Santa movement
		matrix[sy*length+sx] += 1
		sx, sy = advance(sop, sx, sy)
		matrix[sy*length+sx] += 1
		# Robo-santa moevment
		matrix[ry*length+rx] += 1
		rx, ry = advance(rop, rx, ry)
		matrix[ry*length+rx] += 1

	houses = 0
	for i in range(len(matrix)):
		if matrix[i] > 0:
			houses += 1

	print "Part 2: %d houses got at least one present." % houses

def main():
	with open("input") as f:
		route = f.read().strip()

	part1(route)
	part2(route)

	return 0

if __name__ == "__main__":
	exit(main())
