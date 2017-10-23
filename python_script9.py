#! /usr/bin/env python3

#define a function that formats a string of DNA to be a series of liens with a max
#length of 60

import sys
import re
import math

dna = open(sys.argv[1], "r")


def dna_60bp_cutter(dna):
	for line in dna:
		line = line.rstrip(' \n')
		if len(line) < 60:
			full_seq = line
		else:
			trim_seq = line[0:61]
	return trim_seq, full_seq

output = dna_60bp_cutter(dna)
print(output)

#for line in dna:
#	line = line.rstrip(' \n')
#	line = line.join()
#	if len(dna) < 60:
#		trim_seq = dna
#	else:
#		trim_seq = dna[0:61]
