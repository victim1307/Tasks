# Task List : Week 1

### Mapping

Write a small python program to take a few numbers as input and make them print as a list.

Sample Input: `1 22 33 44`
Sample Output: `[1, 22, 33, 44]`

```python
lst = list(map(int, input("Enter the Numbers: ").split()))
print(lst)
```

### Multiply

Write a small python program to take a few `<space>` seperated numbers as input and make the product of those numbers.

Sample Input: `10 20 30 100`
Sample Output: `600000`

Explanation: `10*20*30*100 = 600000`

```python
mul=1
lst = list(map(int, input("Enter the Numbers: ").split()))
for x in lst:
	mul=mul*x
print(mul)
```

### All or Any

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer. Note: Single Digit Numbers are always palindromic

Input Format

The first line contains the space separated list of integers.

Output Format

Print "True" if all the conditions of the problem statement are satisfied. Otherwise, print "False".

Sample Input: `12 9 61 5 14`
Sample Output: `True`

Condition 1: All the integers should be positive (True)
Condition 2: Atleast one of the integers must be palindromic (True)
Since both the conditions are passed that prints "True"

```python
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
else:
	print("False")
```

### Nested Lists

Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format:
```
The first line contains an integer, specifying the number of students.
The subsequent lines describe each student over lines.
- The first line contains a student's name.
- The second line contains their grade.
```

Constraints:
```
There will always be one or more students having the second lowest grade.
```
Output Format:
```
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
```

Sample Input
```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

Sample Output
```
Berry
Harry
```

```python
score_list = [];
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
```

### ginortS

You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string in the following manner
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format:
`A single line of input contains the string .`

Output Format:
`Output the sorted string.`

Sample Input
`Sorting1234`

Sample Output
`ginortS1324`

```python
a,b,c,d=[],[],[],[]
for i in sorted(input()):
    if i.isalpha():
        x = b if i.isupper() else a
    else:
        x = c if int(i)%2 else d
    x.append(i)
print("".join(a+b+c+d))
```
