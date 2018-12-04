#!/usr/bin/env python3
# Day 1: http://adventofcode.com/2018/day/1
def part1():
	with open("input.txt") as data:
		return sum([int(x) for x in data.readlines()])

def part2():
	with open("input.txt") as data:
		changes = [int(x) for x in data.readlines()]
		frequency = 0
		frequencies = set()
		while True:
			for change in changes:
				frequency += change
				if frequency in frequencies:
					return frequency
				frequencies.add(frequency)

def main():
	print("Part 1: {}".format(part1()))
	print("Part 2: {}".format(part2()))

if __name__ == "__main__":
	exit(main())
