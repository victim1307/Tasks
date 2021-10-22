# Nested Lists
# Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Input Format:

# The first line contains an integer, specifying the number of students.
# The subsequent lines describe each student over lines.
# - The first line contains a student's name.
# - The second line contains their grade.
# Constraints:

# There will always be one or more students having the second lowest grade.
# Output Format:

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
# Sample Input

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output

# Berry
# Harry

score_list = [];
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
