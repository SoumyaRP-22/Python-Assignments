"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take an integer input. Check whether the number is prime or not.
Print "Prime" or "Not Prime".

sample input:
Enter an integer: 7
Enter an integer: 10

sample output:
Prime
Not Prime
"""

#SOUTION

x=int(input("Enter an integer:"))
if x==1 or x==0:
    print("Not Prime")
else:
    for i in range(2,x):
        if x%i==0:
            print("Not Prime")
            break

    else:
        print("PRIME")