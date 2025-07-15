"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to remove duplicates but keep the original order from a list of integers, 

sample input:
[1, 2, 2, 3, 4, 4, 5]

sample output:
[1, 2, 3, 4, 5]
"""
# SOLUTION

def remove_dup(list):
    res=[]
    for item in list:
        if  item not in res:
            res.append(item)
    return res

n=int(input('Enter the no of elements:'))
list=[]
print('Enter element for list:')
for i in range(n):
    list.append(input())

result=remove_dup(list)
print(result)