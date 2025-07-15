"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take a string input as password. Check for the following conditions using loop and conditional:

1. Must be at least 8 characters.
2. Must contain at least 1 uppercase letter.
3. Must contain at least 1 digit.
4. Must contain at least 1 special character (@, #, $, %, etc.)

use only loop and conditional statements, and string and it's methods.

sample input:
Enter a password: Abcdef1@
Enter a password: abcdefgh

sample output:
Valid Password
Invalid Password
"""
password=input("Enter the password:")

if len(password)<8:
    print("Invalid Password")

else:
    upper=False
    digit=False
    special=False

    for char in password:
        if char.isupper():
            upper=True
        elif char.isdigit():
            digit=True
        elif char in "@#$%&!":
            special=True

    if upper and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")
