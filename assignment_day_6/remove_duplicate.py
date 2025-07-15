"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 6 **********************************

Problem statement:
Given a tuple of integers, convert it to a tuple without duplicates (preserve order).


sample input:
(1, 2, 2, 3, 4, 4, 5)

sample output:
(1, 2, 3, 4, 5)

"""
# SOLUTION

n=int(input("Enter the no of elements:"))

tup=[]
for i in range(n):
    val=int(input("Enter the value for tuple:"))
    tup.append(val)

list=[]
for val in tup:
    if val not in list:
        list.append(val)

result=tuple(list)
print(result)