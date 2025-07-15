"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
write a function to group items in a list by a specific attribute or property into a dictionary.


sample input:
fruits = {"red": "apple", "yellow": "banana", "red": "cherry", "purple": "grape"}


Sample Output:
{'red': ['apple', 'cherry'], 'yellow': ['banana'], 'purple': ['grape']}

""" 
# SOLUTION

def property(items):
    grouped = {}
    for key, value in items:
        if key in grouped:
            grouped[key].append(value)
        else:
            grouped[key] = [value]
    return grouped

fruits = [
    ("red", "apple"),
    ("yellow", "banana"),
    ("red", "cherry"),
    ("purple", "grape")
]
res=property(fruits)
print(res)