"""
************************* Python internship 2025 *****************************
************************* Assignment Day-1 ***********************************

Problem statement: Take two numbers and an operator (+, -, , /) as input. Perform the operation and print the result.

sample input:
Enter first number: 8  
Enter second number: 2  
Enter operator (+, -, *, /): *

sample output:
The result is: 16

"""
#SOLUTION

a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
op=input("Enter an operator(+,-,*,/):")

if op=='+':
    res=a+b
elif op=='-':
    res=a-b
elif  op=='*':
    res=a*b
elif op=='/':
    res=a/b
else:
    res="INVALID!!"

print("The result is:",res)