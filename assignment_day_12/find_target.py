"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
Implement a function that returns the index of an element in a sorted list using binary search. If not found, return -1.


sample input:
arr = [1, 3, 5, 7, 9]
target=7

sample output:
3

"""
# SOLUTION

def binary_search(arr,tar):
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            l=mid+1
        else:
            h=mid-1

    return -1

arr = [1, 3, 5, 7, 9]
tar=7
print(binary_search(arr,tar))