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
