"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Given a list of integers, sum elements alternatively from start and end.

hint: use while loop with two pointers start and end.


sample input:
Enter the number of element in the list (n): 5
1
2 
3
4
5

sample output:
15  # (1 + 5) + (2 + 4) + 3 = 6 + 6 + 3 = 15

"""
# SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

start=0
end=n-1
sum=0

while start<=end:
    if start==end:
        sum+=list[start]

    else:
        sum+=list[start]+list[end]

    start+=1
    end-=1

print("Sum is:",sum)