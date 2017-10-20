#! /usr/bin/env python3

#define a function that formats a string of DNA to be a series of liens with a max
#length of 60

import sys
import re
import math

#dna = sys.argv[1]


def dna_60bp_cutter(dna):
	for line in dna:
		line = line.rstrip('\n')
#		dna = dna.split()
#		dna = dna.join()
		if len(dna) < 60:
			trim_seq = dna
		else:
			trim_seq = dna[0:61]
	return trim_seq

