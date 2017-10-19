!# usr/bin/env python3


#while loop to print out numbers 1 to 100

count = 1
while count <101:
	print(count)
	count += 1

#while loop to calculate factorial of 1000

count = 1
factorial = 1000
while count < 1000:
	factorial = factorial * count
	count += 1
print(factorial)


#for loop iteration. Find and print even numbers.

numbers =  [101,2,15,22,95,33,2,27,72,15,52]

for num in numbers:
	if num%2  == 0:
		print(num)

#sort list using .sort

numbers.sort()

even_sum = 0
odd_sum = 0
for num in numbers:
	print(num)
	if num % 2 == 0:
		even_sum += num
	if num % 2 == 1:
		odd_sum += num
	
print(even_sum)
print(odd_sum)


#pop() and remove() exercise with number list

print(numbers)
numbers_popped = numbers.pop() #excises last indexed unit in list, stores it in numbers_pop variable
print(numbers)
print(numbers_popped)

print(numbers)
numbers_removed = numbers.remove(2) #removes defined object at lowest index. DOES NOT RETURN THE OBJECT: I.E. CANNOT STORE IN VARIABLE
print(numbers)
print(numbers_removed)


#For loops and range() function

#print numbers 0 to 99 with for loop and range function
for num in range(100):
	print(num)

#print numbers 1 to 100 with for loop and range function
for num in range(101):
	if num > 0:
		print(num)



#create a loop that iterates over below list and prints out position of item in list, lenght of item, and item sequence.
seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

seq_position = 0 #for counting and printing the location of the item in the list, not using zero index for printing
for seq in seqs:
	seq_position +=1 #so as to increase the count and keep proper track of each items position
	print(seq_position,"\t", len(seq),"\t", seq,"\n")
	if seq_position == len(seqs): #stops counting and terminates in tandem with end of list
		break


#creating a shuffled sequence: Fisher-Yates shuffle

import random

sequence = [1, 2, 3, 4]


for seq in sequence:
	count = len(sequence) - 1
	while count > 0:
		positionA = randrange(0,count+1,1)
		sequences[positionA], sequences[count] = sequences[count], sequences[positionA]
		count -= 1
	print(sequence)





#alignment excersise and dictionaries

wH4 = """
AGC----ACCCTCCCACCTCATCCCACCCTTCTGATCTC------------AATCCAACGTCGCATCTCCACCGTCTCGC
G-GATCGACCCAGCGAAGTC----CCTC--CCG-----------------------------------------------
------------------------CCCCCAAAGTCCCCCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCAT--------
----ATAAACCAACCCCCCGCCCTCAGATCCCT-AATCCCATCGCAAGCA--TCAGACTCCCTCCAAAGCAGGCAGCAGC
TCCTCTTCTTC-CTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAA
GGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCA
GGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTC
ATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCG
CCAGGGCCGCACCCTCTACGGCTTCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTG------ATC
TGTGCTGTCGTAGATGAGATTTACTGATTTGGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCAGTGGGCTG--TGTAAT
A-----------------------------------------CCTTGCTCTGTACTTCTGTTCAATGCAATCACTTCTAT
TCTGAA """

hsH4 = """
TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGC
TGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTA
ACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCC--CTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAG
GTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGC
TGCGAGGCTTGCCGTGTT---GCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAA
AGGAGGCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCAC
GGCGTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTA
ATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCG
CCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGT------GTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTC
AGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTT-AATTTCTTAAG-AACACTTAAACGTATGGCAG
TTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCTT-TCAG--CATTACTTAGTGG
TTAAAA"""

#need to remove blank spaces (\n)

whH4 = align1.replace("\n", "")
hsH4 = align2.replace("\n", "")


#compare each index for nucleotide differences
# make a set with each and perform enumerate to ID diferences

index = 0
for nt in align1:
	range(0:len(align1))	
	


#problem 15, dictionary stuff

favs = {}

favs["book"] = "Jitterbug Perfume"
favs["song"] = "Tom Petty - I Won't Back Down"
favs["tree"] = "Cedar"


#problem 15-2, iterator

seq = "AATTGGCC"

A = 0
T = 0
G = 0
C = 0
N = 0
for nt in seq:
	if nt == "A":
		A = A + 1
	elif nt == "T":
		T +=1
	elif nt == "G":
		G +=1
	elif nt == "C":
		C +=1
	else:
		N = N + 1	
	


