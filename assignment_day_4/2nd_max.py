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
25
20
30
10


sample output:
Second maximum number is: 25


"""
#SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

print(list)
list.sort()
list.reverse()
print("Second max no is:",list[1])

