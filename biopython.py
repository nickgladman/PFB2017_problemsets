#! /usr/local/env python3

import sys
import math
import re
from Bio import SeqIO

filename = "/Users/admin/Desktop/files/uniprot_sprot.fasta"

for record in SeqIO.parse(filename, "fasta"):
	print ("ID %s" %  record.id)
	print("Sequence length %i" % len(record))
	print("Sequence alphabet %s" %record.seq.alphabet)


