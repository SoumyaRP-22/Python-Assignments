"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Input a string and print its middle character(s). If the length is even, print the two middle characters; if odd, print one.

sample input:
Enter a string: hello

sample output:
Middle character: l

"""

#SOLUTION

x=input("Enter a string:")
l=len(x)
mid=int(l/2)
if l%2==0:
    print(x[mid-1],x[mid])

else:
    print(x[mid])