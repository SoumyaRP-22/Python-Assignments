"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given two lists (not set) of integers, print the common elements.

sample input:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

sample output:
[3, 4]

"""

#SOLUTION

n=int(input("Enter the no of elements:"))

print("List-1")
list1=[]
for i in range(n):
    val=int(input("Enter the value for list(1):"))
    list1.append(val)
print("List-2")
list2=[]
for i in range(n):
    val=int(input("Enter the value for list(2):"))
    list2.append(val)

common=[]
for val in list1:
    if val in list2:
        common.append(val)

print(common)