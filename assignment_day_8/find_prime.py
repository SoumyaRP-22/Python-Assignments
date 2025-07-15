"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
write a function that takes a number as input and checks the number of prime numbers less than or equal to that number.

sample input:
Enter an integer: 120
Enter an integer: 500

sample output:
30
78
"""
# SOLUTION

def find_prime(n):
    count=0
    for num in range(2,n+1):
        prime=True
        for i in range(2,int(num/2)+1):
            if num%i==0:
                prime=False
                break
        if prime:
            count+=1
    print(count)

n=int(input('Enter a number:'))
find_prime(n)