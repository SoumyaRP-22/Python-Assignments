"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 1 **********************************

Problem statement: 
Ask the user to enter a number and print whether it is even or odd.

sample input:
Enter a number: 7
Enter a number: 6

sample output: 
7 is an odd number.
6 is an even number.
"""

#SOLUTION

num=int(input("Enter a number:"))

if num%2==0:
    print(f"{num} is an even number")

else:
    print(f"{num} is an odd number")