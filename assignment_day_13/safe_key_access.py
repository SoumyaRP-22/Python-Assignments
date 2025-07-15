"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
write a function that takes a list of keys, retrieve values from a given dictionary. 
Use exception handling to return 'key error' if key is missing.


sample input:
keys: ['a', 'b', 'x']
dictionary: {'a': 1, 'b': 2}


sample output:
[1, 2, 'key error']

"""
# SOLUTION

def value(keys,dictionary):
    res=[]
    for key in keys:
        try:
            res.append(dictionary[key])
        except KeyError:
            res.append('key error')
    return res

keys=['a', 'b', 'x']
dictionary={'a': 1, 'b': 2}
output=value(keys,dictionary)
print(output)
