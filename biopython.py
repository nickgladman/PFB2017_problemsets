#! /usr/local/env python3

import sys
import math
import re
from Bio import SeqIO
from Bio import SearchIO

with open("/Users/admin/Desktop/files/uniprot_sprot.fasta") as filename:

	idlist = []

	for (gsname, GN) in re.findall(r"(.{\bOS=.*}({.GN})", filename):
		print(gsname)
		print(GN)
#	for record in SeqIO.parse(filename, "fasta"):
		#print ("ID %s" %  record.id)
		#print("Sequence length %i" % len(record))
		#print("Sequence alphabet %s" %record.seq.alphabet)
		idlist.append(record.id)

	#print(idlist[:10])
		
	
