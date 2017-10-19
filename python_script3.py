#!/usr/bin/env python3

#import modules we have had examples on so far
import sys
import math

#define variable from command line input
x = float(sys.argv[1])

if x > 0:
	print(x, "is a positive number.")
	if x == 50:
		print(x, "is a nice number, but this script can do cool stuff with other values; try another.")
	if x > 50:
		print(x, "is greater than 50.")
		if x%3 == 0:
			print("Also", x, "is divisible by 3.")
	elif x < 50:
		print(x, "is less than 50.")
		if x%2 == 0:
			print("Also", x, "is an even number.")
		else:
			print("Also", x, "is an odd number.")
else:
	print(x, "is a negative number, and we don't like to deal in negatives: this is a happy place.")


