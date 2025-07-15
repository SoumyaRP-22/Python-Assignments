"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Given a list of integers, count how many even and odd numbers are there.
Print the count of even and odd numbers.


sample input:
5
10
15
20
30
10


sample output:
Number of even numbers: 4
Number of odd numbers: 2
"""

# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

even=0
odd=0
for i in range(n):
    if list[i]%2==0:
        even+=1

    else:
        odd+=1

print("Number of even numbers:",even)
print("Number of odd numbers:",odd)