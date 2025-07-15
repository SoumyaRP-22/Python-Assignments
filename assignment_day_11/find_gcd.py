"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 11 **********************************

Problem statement:
Write a function to find the Greatest Common Divisor (GCD) of two positive integers.

Note: The GCD of two numbers is the largest number that divides both of them without leaving a remainder.


sample input:
n1 = 24
n2 = 36

sample output:
output: 12

"""
def gcd(n1,n2):
    if n1<0 or n2<0:
        print("Please enter posive value")
    else:
        if n2==0:
            return n1
        else:
            return gcd(n2,n1%n2)
    
n1=int(input('Enter first num:'))
n2=int(input('Enter second num:'))
print("GCD is:",gcd(n1,n2))