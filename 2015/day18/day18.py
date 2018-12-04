#!/usr/bin/env python
# Day 6: http://adventofcode.com/
from PIL import Image
"""
im = Image.new("RGB", (1000, 1000), "black")
for y in range(1000):
	for x in range(1000):
		im.putpixel((x, y), 0xffffff if lights[y*1000+x] else 0)
print "Saving %d" % n
im.save("part1/%d.png" % n)
n += 1
"""

class LightArray(object):
	def __init__(self, filename="input"):
		self.state = self.read_input(filename)
		self.width = len(self.state[0])
		self.height = len(self.state)

	def read_input(self, filename):
		with open(filename) as f:
			return [x.strip() for x in f.readlines()]

	def on_or_off(self, x, y):
		return False

	def advance(self):
		""" Calculate the next frame
		A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
		A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
		"""
		newstate = ["."*100 for y in range(100)]
		for y in range(self.height):
			for x in range(self.width):
				newstate[y][x] = "#" if self.on_or_off(x, y) else "."
			print newstate[y]
			raw_input()
		self.state = newstate

def main():
	table = LightArray("input")

	print table.state[0]
	table.advance()
	print table.state[0]
	#print table.newstate[0]

	#print table.num_neighbors(1, 1)

	return 0

if __name__ == "__main__":
	exit(main())
