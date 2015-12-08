#!/usr/bin/env python
# Day 8: http://adventofcode.com/

def part1(lines):
	code_size, mem_size = 0, 0
	for l in lines:
		code_size += len(l)
		mem_size += eval("len(" + l + ")")
	return code_size - mem_size

def part2(lines):
	from re import escape
	code_size, escaped_size = 0, 0
	for l in lines:
		code_size += len(l)
		escaped_size += len(escape(l)) + 2
	return escaped_size - code_size

def main():
	with open("input") as f:
		lines = [l.strip() for l in f.readlines()]

	print "Part 1: %d byte difference." % part1(lines)
	print "Part 2: %d byte difference." % part2(lines)

	return 0

if __name__ == "__main__":
	exit(main())
