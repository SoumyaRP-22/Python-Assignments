"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
Given a sorted list with duplicates, count how many times a target number appears using binary search.


sample input:
arr = [1,2,2,2,3,4]
target = 2

sample output:
3

"""
# SOLUTION

arr = [1,2,2,2,3,4]
tar = 2

l=0
h=len(arr)-1
first=-1

while l<=h:
    mid=(l+h)//2
    if arr[mid]==tar:
        first=mid
        h=mid-1
    elif arr[mid]<tar:
        l=mid+1
    else:
        h=mid-1

if  first== -1:
    print('Target not found')
else:
    l=0
    h=len(arr)-1
    last=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==tar:
            last=mid
            l=mid+1
        elif arr[mid]<tar:
            l=mid+1
        else:
            h=mid-1
    
    

count=last-first+1
print(f"Target appears {count} times")
