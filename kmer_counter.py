#! /usr/bin/env python3

import sys
import re
from Bio import SeqIO


####NOTES
#for i in range(0,len(sequence)-kmer_len+1) feeds into kmer=sequence[window_start:window_start + kmer_length]


#this exits the program if not sufficient arguments are provided
#if len(sys.argv) < 4:
#	sys.stderr.write(usage)
#	sys.exit(1)

#sorted hash by value and reverses it in descending order:
#sorted_kmers = sorted(dict, key = lambda x:kmer_dict[x], reverse = True)


kmer_len = int(sys.argv[2]) #this will be a sliding window frame
num_top_kmers = int(sys.argv[3]) #will be how many file to print out--will be a list slice or key-value combination

kmer_dict = {} # key=kmer, value = kmer frequency or count  
def count_kmers(kmer_dict, sequence):
		#the below range() setup makes it so we don't go to the end of the sequence when there is not enough seuqnece left to define a kmer of a given length.
		#The i will become the range
	for i in range(0,len(sequence)-kmer_len+1): #this sets the offset for the sliding window--can't get a two-mer when I'm scanning for a 3mer
		kmer = sequence[i:i+kmer_len] #use the offset "i" to use as the sliding window start point and the user-provided length argument as the end of the sliding window
		if kmer in kmer_dict:
			kmer_dict[kmer] =+1
		else:
			kmer_dict[kmer] = 1		
		return(kmer_dict)
	##additional stuff: look up collections.defaultdict

with open(sys.argv[1]) as filename_fastq:
#	for line in SeqIO.parse(filename_fastq, "fastq"):
	line_count = 0
	for sequence in filename_fastq:
#		print(line)
		sequence = sequence.rstrip()
#		print(line)
		line_count +=1
#		print(line_count)
		if line_count%4 == 2:
			#print(line)
			#print(type(line))
			#print(line[0:5])				
			hash_table = count_kmers(kmer_dict, sequence)
	print(hash_table)

sorted_kmers = sorted(hash_table, key = lambda x:hash_table[x], reverse = True)
print(sorted_kmers[0:num_top_kmers])



#for kmer in sorted_kmers:
#	count = hash_table[kmer]
#	print("()\t()".formate(kmer, count))

##this is totally unsorted
#for (kmer, count) in in hash_table.items():
#	print("()\t().formate(kmer,count) 

#this is good practice when writing code but especially when writing bioinformatics pipelines
sys.exit(0)
