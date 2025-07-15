"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
Write a function that converts a list of strings to integers using map(). 
Handle conversion errors using try inside a helper function.


sample input:
["10", "abc", "25", "4.5"]


sample output:
[10, 'error', 25, 'error']

"""
# SOLUTION

def helper(ls):
    try:
        return int(ls)
    except ValueError:
        return 'error'
    
def convert(str_list):
    return list(map(helper,str_list))

ls=["10", "abc", "25", "4.5"]
output=convert(ls)
print(output)