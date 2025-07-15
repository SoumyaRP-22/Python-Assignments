"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
Given a list of products where each product is represented as a dictionary with keys "name" and "price",
write a Python function to print the names of all products that have a price greater than 10.

sample input:
products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]

sample output:
kiwi
orange
"""
def segregate(products):
    for product in products:
        if product['price']>10:
            print(product['name'])

products = [
    {'name': 'orange', 'price': 20},
    {'name': 'apple', 'price': 8},
    {'name': 'banana', 'price': 10},
    {'name': 'kiwi', 'price': 30}
]
segregate(products)