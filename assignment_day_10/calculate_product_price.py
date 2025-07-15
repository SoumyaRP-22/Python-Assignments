"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
You are given two lists, 
1- product_quantities: the number of units of each product.
2- prices: the price per unit of each product.

Write a Python program using list comprehension and aggregation (like sum) to calculate the total cost of all products.

sample input:
product_quantities = [13, 5, 6, 10, 11]
prices = [1.2, 6.5, 1.0, 4.8, 5.0]

sample output:
Total = 157.1
"""
# SOLUTION

n=int(input('Enter the no of products: '))
quantity=[]
print('Enter the quantity of each product: ')
for i in range(n):
    quantity.append(int(input()))

price=[]
print('Enter the price of each product: ')
for i in range(n):
    price.append(int(input()))

total=sum([x*y for x,y in zip(quantity,price)])
print("Total amount is:",total)