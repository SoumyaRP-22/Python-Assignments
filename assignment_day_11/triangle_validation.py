"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 11 **********************************

Problem statement:
Write a function that takes three sides of a triangle as input and performs the following tasks:
1. Check if the sides form a valid triangle.
2. Classify the triangle as one of the following types (if valid):
    Equilateral - All sides are equal
    Isosceles - Two sides are equal
    Right angled - Follows the Pythagorean Theorem
    Scalene - All sides are different
3. If the triangle is valid and right-angled, compute and print the radius of the circumcenter.
Otherwise, print -1.


sample input:
a = 3
b = 4
c = 5

sample output:
output:
valid
Rightangled
2.5

"""
# SOLUTION
import math
def tri_validation(a,b,c):
    if a+b>c or b+c>a or a+c>b:
        print('Valid')

        if a==b==c:
            print('Equilateral')
        elif a==b or b==c or c==a:
            print('Isosceles')
        else:
            side=sorted([a,b,c])
            a=side[0]
            b=side[1]
            h=side[2]
            if a**2 + b**2==h**2:
                print("Right-angled")
                r=h/2
                print(r)
            else:
                print('Scalene')
    else:
        print('-1')

a=int(input('Enter 1st side of triangle:'))
b=int(input('Enter 2nd side of triangle:'))
c=int(input('Enter 3rd side of triangle:'))

tri_validation(a,b,c)