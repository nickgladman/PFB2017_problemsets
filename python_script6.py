#! /usr/bin/env python3


#open files for reading and writing
Python_05read = open("Python_05.txt", "r")
Python_05write = open("Python_05_uc.txt", "w")

#iterate through files so that I write outpuf of modified Python_05read to Python_05write
for line in Python_05read:
	line = line.upper()
	Python_05write.write(line + "\n")


#always close files
Python_05read.close()
Python_05write.close()

#print output for check
print("Wrote to file 'Python_05_uc.txt'")
