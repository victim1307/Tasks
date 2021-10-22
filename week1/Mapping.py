#Mapping
#Write a small python program to take a few numbers as input and make them print as a list.
#Sample Input: 1 22 33 44 Sample Output: [1, 22, 33, 44]

lst = list(map(int, input("Enter the Numbers: ").split()))
print(lst)
