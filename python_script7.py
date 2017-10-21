#! /usr/bin/env python3

#import sys
#import re
#nobody_file = open(sys.argv[1],)
#fnobody = nobody_file.read()

#print(fnobody)
#for line in re.finditer(r"(Nobody)", fnobody):
#	print(line) #check it's reading the file and identifying the regex "Nobody"
#	print(line.group(1)) #check it's passing through to the regex group1
#	input = line.group(1)
#	input_position_start = line.start(1) + 1
#	print(input, input_position_start)

#nobody_file.close()


#replace "Nobody" with favorite name and write outpu file with that person's name

#import sys
#import re
#nobody_file = open(sys.argv[1],)
#fnobody = nobody_file.read()

#print(fnobody)
#for line in re.finditer(r"Nobody", fnobody):
#       print(line) #check it's reading the file and identifying the regex "Nobody"
#       print(line.group(1)) #check it's passing through to the regex group1
#	new_name = re.sub(r"Nobody", r"Nick", fnobody) #for each line substitue "Nobody" for "Nick", the 3rd option is the string we're iterating through, in this case the one at the top of the loop
#	print(new_name)

##write to existing file in directory
#new_file = open("Nick.txt", "w")
#new_file.write(new_name)
#new_file.close

#print("Wrote to file 'Nick.txt'")

#nobody_file.close()

##Find all header lines in Python_06.fasta

import sys
import re

p6fasta_file = open(sys.argv[1],)
p6fa = p6fasta_file.read()

##this works for capturing only ONE header
#prog = re.compile(r"^>.*")
#result = prog.match(p6fa)
#print(result)

##this also works, but captures every header. This is done by using th re.M modifier, which
## makes the regex ^ search the start of any line, not just the start of the string
found =  re.findall(r"^>.*",p6fa, re.M) #include re.M to properly find headers by searching every line
print(found)
print(type(found))	


p6fasta_file.close()
