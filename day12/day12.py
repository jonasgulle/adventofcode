#!/usr/bin/env python
import simplejson as json
import re

class JsonSummer(object):
	def __init__(self, data):
		self.total = 0
		self.sum_ignore_red(data)

	def sum_ignore_red(self, obj):
		if isinstance(obj, dict):
			values = obj.values()
			if "red" in values:
				return
			else:
				self.sum_sequence(values)
		elif isinstance(obj, list):
			self.sum_sequence(obj)

	def sum_sequence(self, sequence):
		for item in sequence:
			if isinstance(item, int):
				self.total += item
			elif isinstance(item, (dict, list)):
				self.sum_ignore_red(item)

	def __int__(self):
		return self.total

def main():
	with open("input") as f:
		data = f.read()

	print "Part 1: The sum of all integers is %d." % sum(map(int, re.findall(r"-?\d+", data)))
	print "Part 2: The sum is %d excluding all red items." % JsonSummer(json.loads(data))

if __name__ == "__main__":
	exit(main())
