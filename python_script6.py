#! /usr/bin/env python3

import sys

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
p05fa_file = open(sys.argv[1], "r")

#Read into dictionary making value = sequence. Reverse the string value only. Print entire dictionary $

p05 = {}

key = "xxx" #set dictionary key to blank so that it exists in the first place. Will populate down in loop!

for line in p05fa_file:
	if ">" in line: #using header as a way to distinguish ID and sequence
		key = line #set line containing ">" as key
#		print(key, "Nick")
	else: #otherwise if sequence does not contain ">"
		p05[key] = line #make line the first component of the value for the above key
#			print(p05, "Nick")
		if key in p05: #if the key is already in the dictionary (TRUE/FALSE)
			p05[key] += line #add that SEQUENC--it must be sequence since it is not contain ">"
#			print(p05, "Nick")
		else:
			p05[key] = line	#add a new key to dictionary

print(p05[key])


#now iterate over sequence values and do reverse complement program that I've designed before

for seq in p05[key]:
	seq = seq[::-1]

print(p05)
#	compA = seq_comp.replace('A', 't')
#	compAT = compA.replace('T', 'a')
#	compATG = compAT.replace('G', 'c')
#	compATGC = compATG.replace('C', 'g')
#	dna_complement = compATGC.upper()

#print(p05)


p05fa_file.close


