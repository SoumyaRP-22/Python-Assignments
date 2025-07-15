"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given two sets, find elements that are present in either set but not in both.

sample input:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sample output:
(1, 2, 5, 6)

"""
# SOLUTION

n=int(input("Enter the no of element:"))

print("Set-1")
set1=set()
for i in range(n):
    val=int(input("Enter the value for set(1):"))
    set1.add(val)

print("Set-2")
set2=set()
for i in range(n):
    val=int(input("Enter the value for set(2):"))
    set2.add(val)

result=set1^set2

print(result)