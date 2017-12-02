#!/usr/bin/env python
# Day 5: http://adventofcode.com/

def part1(words):
	def isnaughty(s):
		def countvowels(s):
			vowels = 0
			for c in s:
				vowels += 1 if c in "aeiou" else 0
			return vowels

		def doubleletters(s):
			for i in range(len(s) - 1):
				if s[i] == s[i+1]:
					return True
			return False

		def havebadpart(s):
			words = ["ab", "cd", "pq", "xy"]
			for w in words:
				if w in s:
					return True
			return False

		if havebadpart(s):
			return True

		if not doubleletters(s):
			return True

		if countvowels(s) < 3:
			return True
		
		return False

	return sum([isnaughty(w) == False for w in words])

def part2(words):
	def isnice(s):
		candidate = False
		for i in range(len(s)-1):
			pair = s[i:i+2]
			if pair in s[i+2:]:
				candidate = True
				break

		if candidate:
			for i in range(len(s)-2):
				# Test for repeating letters
				if s[i] == s[i+2]:
					return True

		return False

	return sum([isnice(w) for w in words])

def main():
	with open("input") as f:
		words = [x.strip() for x in f.readlines()]

	print "Part 1: %d strings are nice." % part1(words)
	print "Part 2: %d strings are nice." % part2(words)

	return 0

if __name__ == "__main__":
	exit(main())
