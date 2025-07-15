"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Write a function that takes a list of integers, sum elements alternatively from start and end.


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

n=int(input('Enter the no of elements:'))
list=[]
print('Enter value:')
for i in range(n):
    list.append(int(input()))

def alt_sum(list,n):
    i=0
    j=n-1
    sum=0
    while i<=j:
        if i==j:
            sum+=list[i]
        else:
            sum+=list[i]+list[j]
        i+=1
        j-=1

    print('Sum is:',sum)

alt_sum(list,n)    