#!/usr/bin/env python
# Quick and dirty solution for day 10.

def split_equals(s):
	i = 0
	while True:
		if i == len(s)-1:
			yield [str(s[-1])]
			break
		part = []
		while True:
			part += s[i]
			if s[i] != s[i+1]:
				break
			i +=1
		yield part
		i += 1

def look_and_say(n):
	res = []
	for p in split_equals(n):
		res += ([str(len(p)), p[0]])
	return "".join(res)

def main():
	for part, times in enumerate([40, 50]):
		n = "1113222113"
		for i in range(times):
			n = look_and_say(n)
		print "Part %d: Length of result is %d characters." % (part, len(n))
	return 0

if __name__ == "__main__":
	exit(main())
