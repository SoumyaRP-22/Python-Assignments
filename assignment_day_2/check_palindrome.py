"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 2 **********************************

Problem statement: 
Take a string input.
Check if the string is a palindrome (ignore case).
Print "Palindrome" or "Not Palindrome".

sample input:
Enter a string: Madam

sample output:
Palindrome

"""
#SOLUTION

txt=input("Enter a string:")
low=txt.lower()
rev=low[ : :-1]

if rev==low:
    print("Palindrome")

else:
    print("Not Palindrome")
