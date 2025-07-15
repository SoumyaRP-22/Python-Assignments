"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 11 **********************************

Problem statement:
Write a Python program that checks whether two given strings are anagrams of each other.

Two strings are said to be anagrams if they:
    - Contain the same characters
    - Have the same frequency of each character
    - Are of equal length
    - But can be in different order

- learn and write both brute force and optimized code for the problem.
- calculate the time complexity for both the solution.


sample input:
str1 = Listen
str2 = Silent

str1 = Hello
str2 = World

sample output:
Anagram

Not Anagram

"""
# SOLUTION

#Brute Force method
str1=input("Enter string(1):")
str2=input("Enter string(2):")
str1_low=str1.lower()
str2_low=str2.lower()

if len(str1_low)!=len(str2_low):
    print("Not Anagram")

else:
    if sorted(str1_low)==sorted(str2_low):
        print("Anagram")
    else:
        print("Not Anagram")

#Optimized Code
from collections import Counter

str1=input("Enter string(1):")
str2=input("Enter string(2):")
str1_low=str1.lower()
str2_low=str2.lower()

if len(str1_low)!=len(str2_low):
    print("Not Anagram")
else:
    if Counter(str1_low)==Counter(str2_low):
        print("Anagram")
    else:
        print("Not Anagram")