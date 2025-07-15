"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Write a program that swaps the keys and values in a dictionary. If there are duplicate values, the last key will be kept.


sample input:
original = {'a': 1, 'b': 2, 'c': 3}

Sample Output:
{1: 'a', 2: 'b', 3: 'c'}

"""
# SOLUTION

n=int(input('Enter the no of value:'))

original={}
for i in range(1,n+1):
    key=input(f"Enter key {i}:")
    value=input(f"Enter value {i}:")
    original[key]=value

swap={}
for key, value in original.items():
    swap[value]=key

print(swap)
    