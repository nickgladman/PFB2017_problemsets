#!/usr/bin/env python3

#import modules we have had examples on so far
import sys
import math

#define variable from command line input
x = float(sys.argv[1])

#if_else statment that prints out confirmation of truth if True or 'Not True' if False
if x > 7:
	print(x, "is greater than 7")
else:
	print('Not True. ', x, " is not greater than 7")
