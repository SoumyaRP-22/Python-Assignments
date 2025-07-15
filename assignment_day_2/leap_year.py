"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take a year as input and check if it is a leap year.
Note: A leap year is a year that is divisible by 4, except for end-of-century years.

sample input:
Enter year: 2000  

sample output:
Leap Year 

"""
#SOLUTION

year=int(input("Enter a year:"))

if (year%4==0) and (year%100!=0 or year%400==0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")