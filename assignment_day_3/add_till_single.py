"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take an large integer input.Keep adding its digits until the sum becomes a single digit.
Print the final single digit. 


sample input:
Enter a large integer: 9876543210

sample output:
9

"""

#SOLUTION

n=int(input("Enter a large integer:"))

sum=0
while n>=10:
    sum=0
    while n>0:
        sum+=n%10
        n//=10      #remove last digit after addition

    n=sum
print(n)



