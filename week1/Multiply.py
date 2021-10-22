# Multiply
# Write a small python program to take a few <space> seperated numbers as input and make the product of those numbers.
# Sample Input: 10 20 30 100 Sample Output: 600000
# Explanation: 10*20*30*100 = 600000
	
mul=1
lst = list(map(int, input("Enter the Numbers: ").split()))
for x in lst:
	mul=mul*x
print(mul)
