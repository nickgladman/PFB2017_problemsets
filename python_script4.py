
#!/usr/bin/env python3

#import modules we have had examples on so far
import sys
import math

dna = GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG

#counts A and T content
at_content = dna.count('T') + dna.count('A')

#counts C and G content
cg_content = dna.count('C') + dna.count('G')

#complement ATGC sequence in dna by sequential replacing USING CASE AS A DINSTINGUISHER--use loop later.
compA = dna.replace('A', 't')
compAT = compA.replace('T', 'a')
compATG = compAT.replace('G', 'c')
compATGC = compATG.replace('C', 'g')

dna_complement = compATGC.upper()

#reversing a string [begin:end:step] is extended slice syntax. Leaving begin and end off and specifying a step of -1, it reverses a string

dna_reverse_complement = dna_complement[::-1]

#EcoR1 recognition start and site report. EcoR1 = 5' GAATTC 3'

ecor1 = "GAATTC"
ecor1_start_site = 1 + int(dna.find("GAATTC"))
ecor1_end_site = ecor1_start_site + 5

ecor1_print = '''The recognition sequence for EcoR1 is {0}.
The recognition start site is located at {1} and ends at {2}.'''

print(ecor1_print.format(ecor1, ecor1_start_site, ecor1_end_site))




