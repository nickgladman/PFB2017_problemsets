#! /usr/bin/env python3

import sys, os, re


myDict = {}
fh = open(sys.argv[1])
for line in fh:
	line = line.rstrip()
	fields = line.split("\t")

	read_name = fields[0]
	combo_name = fields[2]
	(geneID, transcriptID) = combo_name.split("^")
	
	if geneID not in myDict:
		myDict[geneID] = set() #pipes unique geneIDs to a set for easy consumption

	myDict[geneID].add(read_name)

gene_ids = sorted(myDict, key = lambda x: len(myDict[x]), reverse = True)

#print(myDict)
for gene_id in gene_ids:
	mySet = myDict[geneID]
	num_reads = len(mySet)

	print("()\t()".format(geneID, num_reads))

fh.close()
