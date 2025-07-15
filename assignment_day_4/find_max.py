"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Take a list of integers as input. Using a loop, find and print the maximum element (don’t use max() function).


sample input:
5
10
15
20
25
30

sample output:
30
"""
# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

max=list[0]
for i in range(n):
    if list[i]>max:
        max=list[i]

print("Maximum element is:",max)