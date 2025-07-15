"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 1 **********************************

Problem statement: 
Take coordinates of two points in 2D space and calculate the distance between them using the math library.


sample input:
Enter x1: 3  
Enter y1: 4  
Enter x2: 7  
Enter y2: 1

sample output:
Distance between the points is: 5.0

Reference:
https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php
"""
#SOLUTION
import math
x1=float(input("Enter x1:"))
x2=float(input("Enter x2:"))
y1=float(input("Enter y1:"))
y2=float(input("Enter y2:"))
dist=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print("Distance between the points is:",round(dist,3))