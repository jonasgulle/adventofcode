#!/usr/bin/env python
# Day 6: http://adventofcode.com/
from PIL import Image

def parse_row(row):
	for o in ["turn off", "turn on", "toggle"]:
		if o in row:
			fromto = []
			for i in [x.strip() for x in row[len(o)+1:].split("through")]:
				fromto.append(map(int, i.split(",")))
			return {
				"command": o,
				"from": fromto[0],
				"to": fromto[1]
			}
	raise Exception("Parse error")

def apply1(lights, cmd):
	# Not really optimized for speed.
	for y in range(cmd["from"][1], cmd["to"][1]+1):
		for x in range(cmd["from"][0], cmd["to"][0]+1):
			ofs = y*1000+x;
			if cmd["command"] == "turn off":
				lights[ofs] = 0
			elif cmd["command"] == "turn on":
				lights[ofs] = 1
			elif cmd["command"] == "toggle":
				lights[ofs] = 0 if lights[ofs] else 1


def apply2(lights, cmd):
	# Not really optimized for speed.
	for y in range(cmd["from"][1], cmd["to"][1]+1):
		for x in range(cmd["from"][0], cmd["to"][0]+1):
			ofs = y*1000+x;
			if cmd["command"] == "turn off":
				if lights[ofs] > 0:
					lights[ofs] -= 1
			elif cmd["command"] == "turn on":
				lights[ofs] += 1
			elif cmd["command"] == "toggle":
				lights[ofs] += 2

def read_input():
	with open("input") as f:
		return [parse_row(x.strip()) for x in f.readlines()]

def part1():
	lights = bytearray(1000*1000)
	n = 0
	for cmd in read_input():
		apply1(lights, cmd)
		"""
		im = Image.new("RGB", (1000, 1000), "black")
		for y in range(1000):
			for x in range(1000):
				im.putpixel((x, y), 0xffffff if lights[y*1000+x] else 0)
		print "Saving %d" % n
		im.save("part1/%d.png" % n)
		n += 1
		"""

	# Now count the lit lights
	return sum(lights)

def part2():
	lights = bytearray(1000*1000)
	n = 0
	for cmd in read_input():
		apply2(lights, cmd)
		"""
		im = Image.new("RGB", (1000, 1000), "black")
		for y in range(1000):
			for x in range(1000):
				v = lights[y*1000+x]*10
				im.putpixel((x, y), (v, v, v))
		print "Saving %d" % n
		im.save("part2/%d.png" % n)
		n += 1
		"""

	# Now count the total brightness
	return sum(lights)

def main():
	print "Part 1: %d lights are lit" % part1()
	print "Part 2: %d is the total brightness" % part2()
	return 0

if __name__ == "__main__":
	exit(main())
