"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
Write a function that takes a list of numbers and divides 100 by each. 
Skip any division by zero using exception handling.


sample input:
[25, 0, 10, -5]


sample output:
[4.0, 'error', 10.0, -20.0]

"""
# SOLUTION

def division(nums):
    res=[]
    for num in nums:
        try:
            res.append(100/num)
        except ZeroDivisionError:
            res.append('error')

    return res

number=[25, 0, 10, -5]
output=division(number)
print(output)