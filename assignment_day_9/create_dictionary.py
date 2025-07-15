"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to convert a given list to a dictionary.

sample input:
["name=Akasha", "age=30", "city=Hyderabad"], 

sample output:
{
    'name': 'Akasha',
    'age': 30,
    'city': 'Hyderabad'
}
"""
# SOLUTION

def create_dict(list):
    res={}
    for item in list:
        if '=' in item:
            key,val=item.split('=',1)
            res[key]=val
    return res

list=["name=Akasha", "age=30", "city=Hyderabad"]
result=create_dict(list)
print(result)