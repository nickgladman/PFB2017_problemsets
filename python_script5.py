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

