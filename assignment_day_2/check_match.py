"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take two integer inputs and check if they have the same last digit. Print "Match" if they do, otherwise print "No Match".
don't use loop or any built-in functions.

sample input:
Enter first number: 123  
Enter second number: 93 

sample output:     
Match
"""
#SOLUTION

a=int(input("Enter an integer:"))
b=int(input("Enter an integer:"))

if a%10==b%10:
    print("Matched")
else:
    print("Does not Match")