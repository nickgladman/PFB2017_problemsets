#! /usr/bin/env python3

import sys
import re

#open files for reading and writing
#Python_05read = open("Python_05.txt", "r")
#Python_05write = open("Python_05_uc.txt", "w")

#iterate through files so that I write outpuf of modified Python_05read to Python_05write
#for line in Python_05read:
	#line = line.upper()
	#Python_05write.write(line + "\n")


#always close files
#Python_05read.close()
#Python_05write.close()

#print output for check
#print("Wrote to file 'Python_05_uc.txt'")



#Open and print the rev complement of each sequence in Python_05.fasta
#p05fa_file = open(sys.argv[1], "r")

#Read into dictionary making value = sequence. Reverse the string value only. Print entire dictionary to STDOUT

#p05 = {}

#this code was designed with a different data manipulation in mind
#use the consistent header of FASTA to your advantage and designate key-value distinction from that foundation
#for line in p05fa_file:
	#line = line.rstrip() #removes whitespace from start and end and retunrs
	#print(line, "Nick")
	#id, seq = line.split() #generates substrings separated by whitespace, now I have substrings I can pass through to key:value pairs
	#print(line, "Nick")
	#p05[id] = seq
	#print(line, p05)

	#for seq in p05:
		#seq_comp = seq[::-1]		
		#compA = seq_comp.replace('A', 't')
		#compAT = compA.replace('T', 'a')
		#compATG = compAT.replace('G', 'c')
		#compATGC = compATG.replace('C', 'g')
		#dna_complement = compATGC.upper()

#always close!!!
#p05fa_file.close()

#use the consistent header of FASTA to your advantage and designate key-value distinction from that fo$

#Open and print the rev complement of each sequence in Python_05.fasta
#p05fa_file = open(sys.argv[1], "r")

#Read into dictionary making value = sequence. Reverse the string value only. Print entire dictionary $

#p05 = {}

#key = "xxx" #set dictionary key to blank so that it exists in the first place. Will populate down in loop!

#for line in p05fa_file:
#	if  ">" in line: #using header as a way to distinguish ID and sequence
#		key = line #set line containing ">" as key
#		print(key, "Nick")
#	else: #otherwise if sequence does not contain ">"
#		line = line[::-1] #reverses sequence
#		#complementing the nucleotides should occur here.
#		p05[key] = line #make line the first component of the value for the above key
#			print(p05, "Nick")
#		if key in p05: #if the key is already in the dictionary (TRUE/FALSE)
#			p05[key] += line #add that SEQUENC--it must be sequence since it is not contain ">"
#			print(p05, "Nick")
#		else:
#			p05[key] = line	#add a new key to dictionary
		
#print(p05, "Nick")

#p05fa_file.close


#Problem set 5.5: gene lists
# create sets for the three alpaca gene sets I downloaded from Ensembl Biomart

#go line by line and add each gene name as the key value for the set

all = set()   
stem = ()   
pig = ()  

with open("alpaca_all_genes.tsv", "r") as file_all_genes:
	for line in file_all_genes:
		line = line.rstrip()
		all.add(line) #.add() is a method for sets. Like .append() for lists.		

#print(all)

with open("alpaca_pigmentation_genes.tsv", "r") file_pig_genes:
	for line in file_pig_genes:
		line = line.rstrip()
		pig.add(line)


with open("alpaca_stemcellproliferation_genes.tsv", "r") file_stem_genes
	for line in file_pig_genes:
		line = line.rstrip()
		pig.add(line)






#print(all)
#print(stem)
#print(pig)

##file closes are unnecessary when using with open() as file_object syntax above
#file_all_genes.close()
#file_pig_genes.close()
#file_stem_genes.close()
