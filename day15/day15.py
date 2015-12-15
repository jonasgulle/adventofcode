#!/usr/bin/env python
from collections import defaultdict
from itertools import product

ingredients = defaultdict(dict)

def calc_ingredient_sum(ingredients, teaspoons):
	return sum([a*b for a, b in zip(ingredients, teaspoons)])

def get_property(prop):
	return [i[prop] for i in ingredients.values()]

def main():
	with open("input") as f:
		data = [l.strip().split(", ") for l in f.readlines()]

	# Extract all our ingredients into a nice dict
	for i in data:
		name, key = i[0].split(": ")
		for j in [key] + i[1:]:
			k, v = j.split(" ")
			ingredients[name][k] = int(v)

	max_sum = 0
	max_calorie_sum = 0
	for s in product(range(1, 98), repeat=4):
		if sum(s) != 100:
			continue
		capacity = calc_ingredient_sum(get_property("capacity"), s)
		durability = calc_ingredient_sum(get_property("durability"), s)
		flavor = calc_ingredient_sum(get_property("flavor"), s)
		texture = calc_ingredient_sum(get_property("texture"), s)
		calories = calc_ingredient_sum(get_property("calories"), s)

		if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
			continue
		else:
			max_sum = max(capacity*durability*flavor*texture, max_sum)
			if calories == 500:
				max_calorie_sum = max(capacity*durability*flavor*texture, max_calorie_sum)

	print "Part 1: The best cookie would score %d." % max_sum
	print "Part 2: The best meal replacement cookie would score %d." % max_calorie_sum

	return 0

if __name__ == "__main__":
	exit(main())
