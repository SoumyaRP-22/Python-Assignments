"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Write a program that performs various set operations (union, intersection, difference) on two sets based on a specified operation parameter.


sample input:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
operation = "symmetric_difference"

Sample Output:
{1, 2, 5, 6}

"""
# SOLUTION

n=int(input("Enter the no elements:"))

print("For SET-1 enter the values:")
set1=set()
for i in range(n):
    set1.add(int(input()))

print("For SET-2 enter the values")
set2=set()
for i in range(n):
    set2.add(int(input()))

op=input('Enter the operation to perform:')

if op=='union':
    res=set1.union(set2)
elif op=='intersection':
    res=set1.intersection(set2)
elif op=='difference':
    res=set1.difference(set2)
elif op=='symmetric difference':
    res=set1.symmetric_difference(set2)

print(res)

