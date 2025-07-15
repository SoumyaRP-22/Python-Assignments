"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 13 **********************************

Problem statement: 
write a function that takes list of ages, filter only valid ages (integers between 0-120).
use filter function for this.

sample input:
[25, -5, 130, 90]


sample output:
[25, 90]

"""
def filt(ls):
    return 0<= ls <=120

age=[25, -5, 130, 90]
new=list(filter(filt,age))
print(new)