"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to find all common elements between two lists.
Don't set functions

sample input:
["apple", "banana", "cherry"]
["banana", "cherry", "date"]

sample output:
["banana", "cherry"]
"""
# SOLUTION

def find_comm(lst1,lst2):
    common=[]
    for item in lst1:
        if item in lst2 and item not in common:
            common.append(item)
    return common

n=int(input('Enter the no of elements:'))
lst1=[]
print('Enter element for list(1):')
for i in range(n):
    lst1.append(input())

lst2=[]
print('Enter element for list(2):')
for i in range(n):
    lst2.append(input())

result=find_comm(lst1,lst2)
print(result)