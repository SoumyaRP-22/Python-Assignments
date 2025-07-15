"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
Given a list of words, return the kth unique word based on order of first appearance. 
If less than k unique words exist, return None.

hint- dont use set, it will remove the order of the elements.

sample input:
words = ["apple", "banana", "apple", "cherry", "banana", "date"]
k = 2

sample output:
"cherry"
"""
# SOLUTION

words = ["apple", "banana", "apple", "cherry", "banana", "date"]
k = 2

unique=[]
for word in words:
    if word not in unique:
        unique.append(word)

if k < len(unique):
    print(unique[k-1])
else:
    print(None)