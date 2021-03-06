#!/usr/bin/env python
# Day 1: http://adventofcode.com/

# Part 1
with open("input") as f:
	data = f.read()
print "Santa is on floor %d" % (data.count('(') - data.count(')'))

# Part 2
floor = 0
for i, c in enumerate(data):
	if c == '(': floor += 1
	elif c == ')': floor -= 1
	if floor == -1:
		print "First time in basement is position %d" % (i+1)
		break
