"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Take a list of integers. Find the element that occurs more than n/2 times. 
If no such element exists, print "No Majority". 
where n is the number of elements in the list.


sample input:
Enter the number of element in the list (n): 5
1
2
3 
1 
1

sample output:
1

"""
#SOLUTION

list=[]
n=int(input("Enter no of elemennts:"))

for i  in range(n):
    val=int(input("Enter the value:"))
    list.append(val)

majority=False
for num in list:
    if list.count(num)>n//2:
        majority=True
        break

if majority:
    print(num)

else:
    print("No Majority")

    