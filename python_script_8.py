#! /usr/bin/env python3

import sys
import re

##Python 8 problem sets

#1.0 Take a mulit-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format
# need to go through the FASTA file line at a time, using the first line ID (header)
# as the dictionary key for nucleotide value. In turn the nucleotide value also functions as 
#the dictionary name for the nucleotide content subdictionary. Each A T G C within the nucleotide
#content dictionary functions as a separate key, to which the value is the occurrence of each
#nucleotide within the sequence.
#fasta[gene_name][nt] = {A:, # T:, # G: #, C: #}

#construct empty dictionary dataframe
#populate each dictionary with proper key-values
#count nucleotides and add into lowest dictionary level


fasta = {} #highest level dictionary


for line in sys.argv[1]:
	line = line.split()
	if r"(^>.*\s)" not in line:
		group(1)= fasta[]

print(fasta)



#for line in sys.argv[1]:
#        line = line.split()
#        if r"(^>.*\s)" in line:
#                line = fasta[line]
#
#print(fasta)

