""" 
************************* Python internship 2025 *****************************
************************* Assignment Day-1 ***********************************

Problem statement: Prompt the user to enter the diameter of a circle, then calculate and display its circumference.
Sample Input:
Enter the diameter of the circle: 10

sample Output:
The circumference of the circle is: 31.42

(Assuming π ≈ 3.1416 and rounding to 2 decimal places)
"""

#SOLUTION

dia=float(input("Enter the diameter of the circle:"))
cir=3.1416*dia
print("Circumference of the circle is:",round(cir,2))