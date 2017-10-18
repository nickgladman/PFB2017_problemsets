#! /usr/bin/env python3

import sys

#user inputs will create a range of values to use
number1 = int(sys.argv[1])
number2 = 1 + int(sys.argv[2])

for num in range(number1, number2, 1):
	print(num)
