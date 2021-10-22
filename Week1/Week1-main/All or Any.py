# All or Any
# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer. Note: Single Digit Numbers are always palindromic

# Input Format

# The first line contains the space separated list of integers.

# Output Format

# Print "True" if all the conditions of the problem statement are satisfied. Otherwise, print "False".

# Sample Input: 12 9 61 5 14 Sample Output: True

def pal(num) :
    rev_num = 0;
    while (num > 0) :
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

lst = list(map(int, input("Enter the Numbers: ").split()))
for x in lst:
	if x==pal(x):
		print("True")
		break
	elif x==lst[len(lst)-1]:
		print("False")
		break
