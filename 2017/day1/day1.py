#!/usr/bin/env python
# Day 1: http://adventofcode.com/2017/day/1
import unittest

def captcha_part1(numbers):
	numbers = [ord(c) - ord("0") for c in numbers]
	result = 0
	for i, a in enumerate(numbers):
		b = numbers[(i + 1) % len(numbers)]
		if a == b:
			result += a
	return result

def captcha_part2(numbers):
	numbers = [ord(c) - ord("0") for c in numbers]
	result = 0
	for i, a in enumerate(numbers):
		b = numbers[(i + (len(numbers) / 2)) % len(numbers)]
		if a == b:
			result += a
	return result

class Tests(unittest.TestCase):
	def test_part1(self):
		self.assertEqual(captcha_part1("1122"), 3)
		self.assertEqual(captcha_part1("1111"), 4)
		self.assertEqual(captcha_part1("1234"), 0)
		self.assertEqual(captcha_part1("91212129"), 9)

	def test_part2(self):
		self.assertEqual(captcha_part2("1212"), 6)
		self.assertEqual(captcha_part2("1221"), 0)
		self.assertEqual(captcha_part2("123425"), 4)
		self.assertEqual(captcha_part2("123123"), 12)
		self.assertEqual(captcha_part2("12131415"), 4)

def main():
	unittest.main(exit=False)

	with open("input.txt") as f:
		digits = f.read().strip()

	print "Part 1: Answer is", captcha_part1(digits)
	print "Part 2: Answer is", captcha_part2(digits)

if __name__ == "__main__":
	exit(main())
