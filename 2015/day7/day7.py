#!/usr/bin/env python
# Day 7: http://adventofcode.com/
from ctypes import c_ushort as u16

class Wires(object):
	def __init__(self, filename):
		with open(filename) as f:
			lines = [[j.strip() for j in l.split("->")] for l in f.readlines()]
		self.regs = dict((res, op) for (op, res) in lines)
		self.reset()

	def reset(self):
		self.results = {}

	def signal(self, wire):
		try:
			return int(wire)
		except ValueError:
			pass

		if wire not in self.results:
			tokens = self.regs[wire].split(" ")
			if len(tokens) == 1:
				res = self.signal(tokens[0])
			else:
				# OR, AND, RSHIFT or LSHIFT
				if len(tokens) == 3:
					if tokens[1] == "OR":
						res = self.signal(tokens[2]) | self.signal(tokens[0])
					elif tokens[1] == "AND":
						res = self.signal(tokens[2]) & self.signal(tokens[0])
					elif tokens[1] == "LSHIFT":
						res = self.signal(tokens[0]) << int(tokens[2])
					elif tokens[1] == "RSHIFT":
						res = self.signal(tokens[0]) >> int(tokens[2])
					else:
						raise Exception("Invalid opcode: %s" % l)
				elif len(tokens) == 2:
					if tokens[0] == "NOT":
						return ~self.signal(tokens[1])

			# Memoization
			self.results[wire] = res

		return self.results[wire]

def main():
	w = Wires("input")
	sig_a = w.signal("a")
	print "Part 1: The signal on wire a is: %d" % sig_a
	w.reset()
	w.results["b"] = sig_a
	print "Part 2: The signal on wire a is: %d" % w.signal("a")
	return 0

if __name__ == "__main__":
	exit(main())
