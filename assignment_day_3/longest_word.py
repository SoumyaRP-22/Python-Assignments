"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Take a string input (a sentence). Find the longest word in the sentence and print it.

Use only loop and conditional statements. don't use any built-in functions, like split.


sample input:
Enter a sentence: The quick brown fox jumped over the lazy dog      
Enter a sentence: Python is a great programming language

sample output:
jumped
programming

"""
#SOLUTION

sent=input("Enter a sentence:")

word=sent.split()
long=""

for w in word:
    if len(w)>len(long):
        long=w

print(long)