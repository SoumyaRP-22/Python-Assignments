"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take three numbers and print the largest one using only if-else (no built-in functions like max()).

sample input:
Enter numbers: 12, 45, 33  

sample output:
Largest number is: 45  

"""
#SOLUTION

x=int(input("Enter a no:"))
y=int(input("Enter a no:"))
z=int(input("Enter a no:"))

if x>y and x>z:
    print("Largest number is",x)

elif y>x and y>z:
    print("Largest number is",y)

else:
    print("Largest number is",z)