"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 9 **********************************

Problem statement: 
write a function to return a dictionary with the count of each character in the given sentence.

sample input:
"apple"

sample output:
{
    'a': 1,
    'p': 2,
    'l': 1,
    'e': 1
}
"""
# SOLUTION

def count_char(s):
    count={}
    for char in s:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    return count

s=input("Enter a word:")
output=count_char(s)
print(output)