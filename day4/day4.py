#!/usr/bin/env python
# Day 4: http://adventofcode.com/
from hashlib import md5

def crack(key, numzeroes, start=0):
	match = "0"*numzeroes
	while True:
		md5hash = md5("%s%d" % (key, start)).hexdigest()
		if md5hash[0:numzeroes] == match:
			return (start, md5hash)
		start += 1

def main():
	# Test cases
	print "Test cases"
	print crack("abcdef", 5, 600000)
	print crack("pqrstuv", 5, 600000)
	# Part 1
	print "Part 1"
	print crack("ckczppom", 5)
	# Part 2
	print "Part 2"
	print crack("ckczppom", 6)

	return 0

if __name__ == "__main__":
	exit(main())
