"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Take a list of integers. Find and print the maximum product that can be formed by multiplying any two different elements.


sample input:
Enter the number of element in the list (n): 5
3
5 
-2 
9 
-10

sample output:
90

"""
# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

max=0
for i in range(n):
    for j in range(i+1,n):
        product=list[i]*list[j]
        if product>max:
            max=product

print("The max product is:",max)