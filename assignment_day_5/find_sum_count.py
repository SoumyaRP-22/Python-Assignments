"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Given a tuple of integers and an integer K, count the number of pairs whose sum is divisible by K.

sample input:
Enter the number of element in the list: 5
2 
3 
4 
6 
8
Enter the value of K: 4

sample output:
3 #(2,6), (4,8), (8,4)

"""
# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

list=tuple(list)
k=int(input("Enter the value of k:"))
count=0
for i in range(n):
    for j in range(i+1,n):
        if (list[i]+list[j])%k==0:
            count+=1

print("No of pairs is:",count)