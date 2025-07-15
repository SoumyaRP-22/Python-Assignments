"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given a list of integers and a target sum, check if any two distinct elements sum up to the target.

sample input:
[2, 4, 5, 7, 11]

sample output:
9

"""
#SOLUTION

n = int(input("Enter number of elements in the list: "))
numbers = []

print("Enter the numbers:")
for i in range(n):
    numbers.append(int(input()))

target = int(input("Enter the target sum: "))

found = False
for i in range(n):
    for j in range(i + 1, n): 
        if numbers[i] + numbers[j] == target:
            found = True
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")
