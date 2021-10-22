# ginortS
# You are given a string S. S contains alphanumeric characters only. Your task is to sort the string in the following manner All sorted lowercase letters are ahead of uppercase letters. All sorted uppercase letters are ahead of digits. All sorted odd digits are ahead of sorted even digits.

# Input Format: A single line of input contains the string .

# Output Format: Output the sorted string.

# Sample Input Sorting1234

# Sample Output ginortS1324

a,b,c,d=[],[],[],[]
for i in sorted(input()):
    if i.isalpha():
        x = b if i.isupper() else a
    else:
        x = c if int(i)%2 else d
    x.append(i)
print("".join(a+b+c+d))
