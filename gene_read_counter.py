#! /usr/bin/env python3

import sys
import re
from Bio import Seq

#Task:
#Write a python program that reads in the 'bowtie2.bam' file and generates a table containing the number of reads mapped to each gene.

sam_file = open(sys.argv[1])

gene_with_transcript_list = []

#####################
##the below code performs a different task than what was asked in the instructions: it parses the sam file, but it attributes reads based on a different list element (a substring of column 3).
for line in sam_file:
	line = line.rstrip() #remove newlines
	line = line.split('\t') #split on tabs to make list
#	print(type(line)) #check
#	print(len(line)) #check
	if line[2] not in gene_with_transcript_list:
		gene_with_transcript_list.append(line[2]) #append 3rd column to list if not already in list


#print(gene_with_transcript_list[0:10]) #check list makeup
#print(len(gene_with_transcript_list)) #check list makeup

gene_read_dict = {} # key = geneID, value = count
gene_count = 1

#spliting gene from transcript ID. There is a faster way to do this and it can be incoporated into the above for loop.
for geneID in gene_with_transcript_list:
	geneID =geneID.split("^")
	#print(geneID)
	#print(len(geneID))
	if geneID[0] in gene_read_dict:
		gene_count +=1
		gene_read_dict[geneID[0]] = gene_count
	else:
		gene_read_dict[geneID[0]] = 1


print(gene_ids)
print(gene_read_dict)

#sorts the dictionary by value 
#sorted_gene_read_dict = sorted(gene_read_dict, key = gene_read_dict[geneID], reverse = True)
#sorted_gene_read_dict = sorted(gene_read_dict.values()) #this will return a list of values

#print(sorted_gene_read_dict)

sam_file.close()



###########################################


###Code from lecturer

#Same as mine for reading in and spliting
#for loop:

myDict = {}
#fh = open(sys.argv[1])
#for line in fh:
#	line = line.rstrip()
#	fields = line.split("\t")

#	read_name = line[0]
#	combo_name = line[2]
	
#	(geneID, transcriptID) = combo_name.split("^")

#	if geneID not in mydict:
#		myDict[geneID] = set() #pipes unique geneIDs to a set for easy consumption

#	myDict[geneID].add(read_name)

#gene_ids = sorted(myDict, key = lambda x: len(myDict[x]), reverse = True)

#for gene_id in gene_ids:
#	mySet = myDict[geneID]
#	num_reads = len(mySet)

#	print("()\t()".format(geneID, num_reads)
