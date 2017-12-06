#!/usr/bin/env python
# Day 2: http://adventofcode.com/2017/day/2
import unittest

class Tests(unittest.TestCase):
	def test_part1(self):
		self.assertEqual(checksum_part1("5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8"), 18)
	def test_part2(self):
		self.assertEqual(checksum_part2("5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"), 9)

def checksum_part1(data):
	checksum = 0
	lines = map(lambda x: x.split("\t"), data.split("\n"))
	for line in lines:
		digits = [int(x) for x in line]
		checksum += max(digits) - min(digits)
	return checksum

def checksum_part2(data):
	checksum = 0
	lines = map(lambda x: map(int, x.split("\t")), data.split("\n"))
	for digits in lines:
		for i, n in enumerate(digits[:-1]):
			for m in digits[i+1:]:
				if n > m:
					if n % m == 0:
						checksum += int(n/m)
				else:
					if m % n==0:
						checksum += int(m/n)
	return checksum

def main():
	unittest.main(exit=False)

	with open("input.txt") as f:
		data = f.read()

	print "Part 1: The answer is", checksum_part1(data)
	print "Part 2: The answer is", checksum_part2(data)

if __name__ == "__main__":
	exit(main())
