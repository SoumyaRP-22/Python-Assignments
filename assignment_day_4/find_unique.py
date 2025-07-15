"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 4 **********************************

Problem statement: 
Take a list of integers as input. Create a new list that contains only unique elements (preserving original order).
Use loops and conditionals only — don’t use set().


sample input:
5
10
10
15
20
20
30
10


sample output:
5
10
15
20
25
30
"""
# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

unique=[]

for num in list:
    if num not in unique:
        unique.append(num)

print("The original list:\n",list)
print("The unique list:\n",unique)