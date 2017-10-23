#! /usr/bin/env pyton3

import sys
import math
import re
import statistics

fasta =  open(sys.argv[1], "r")

linecount = 0
seq = []
seqcount = 0

#for i, line in enumerate(fasta):
#	line = line.rstrip('\n')
#	if i%3 == 0 and i%2 != 0: #for every 3rd line
#		seqcount += 1
#		seq.append(len(line))

#print(seq)	
#print(seqcount)

#print(statistics.mean(seq))
#print(statistics.stdev(seq))

#fasta.close()



#trim a fastq so that it removes every value with a Q < 20.

remindex = []

for i, line in enumerate(fasta):
	if i%4 == 0:
		line.rstrip()
		line.join('\n')
#		print(i)
#		print(line)
		#Illumina Q = ASCII value. Q = 64 + Phredd score
#		if line != remindex:
		remindex.append(line)	

print(remindex[:5])

ascii_index = []

for item in remindex:
	for pos in item:
		pos = ord(pos)
		ascii_index.append(pos)

print(ascii_index[:58])
print(ascii_index[56:120])
index_list = []

for i, line in enumerate(ascii_index):
	if line < 84:
		index_list.append(i)

print(index_list[:5])	

#for i, line in enumerate(fasta):
#	if i%4 == 0:
#		for i, char in enumerate(line):
#			if i = 


fasta.close()
