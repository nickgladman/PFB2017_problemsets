#! /usr/local/evn python3

import sys
import math
import re


with open(sys.argv[1], "r") as filename:
	
	fileinfo = []
	fieldnames =[]
	rand5_200 = {}	
#	rand5_800 = {}
	if sys.argv[2] == "rand5-200":
		for line in filename:
			line = line.strip('\n')
			if line.startswith(r"# Fields: "): #captures header row
				line.split(' ') #doesn't do much I think
				fieldnames = str(line) #generates the line into a string
				fieldnames = fieldnames.strip().split(",") #splits and delimits the string by the commas and feeds them into a list, 11 commas = 12 items in list
#				print(len(fieldnames), fieldnames, type(fieldnames)) ##check
			elif "#" not in line: #checking for lines that contain our sequence data
				line = line.split('\t')	#splitting on that delimiter, which is tab		
				fileinfo.append(line) # THIS GENERATES A LIST OF LISTS: EACH ROW IS A LIST USING THE TAB AS A SEPARATOR: 12 ITEMS PER NESTED LIST = 12 COLUMNS
	rand5_200 = dict(zip(fieldnames, fileinfo)) ####THIS WILL NOT WORK: IT WILL WRITE OVER THE KEY-VALUE COMBINATION BECAUSE IT JUST REPLACES THE OLD KEYS
						#####WITH NEW ONES AND REPOPULATES WITH THE LAST LIST FOR THE VALUES.				

#THIS IS FOR THE OTHER HALF OF THE SCRIPT FOR TAKING THE 2ND USER ARGUMENT 'RAND5-800'. SAME AS ABOVE.
	elif sys.argv[2] == "rand5-800":
		for line in filename:
			line = line.strip('\n')
			if line.startswith(r"# Fields: "): #captures header row
				line.split(' ') #doesn't do much I think
				fieldnames = str(line) #generates the line into a string
				fieldnames = fieldnames.strip().split(",") #splits and delimits the string by the commas and feeds them into a list, 11 commas = 12 items in list
				print(len(fieldnames), fieldnames, type(fieldnames)) ##check
			elif "#" not in line: #checking for lines that contain our sequence data
				line = line.split('\t') #splitting on that delimiter, which is tab
				fileinfo.append(line) # THIS GENERATES A LIST OF LISTS: EACH ROW IS A LIST USING THE TAB AS A SEPARATOR: 12 ITEMS PER NESTED LIST = 12 COLUMNSfor line in filename:

#print(rand5_800)
print(rand5_200)
