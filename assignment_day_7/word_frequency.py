"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 7 **********************************

Problem statement: 
Counts the frequency of each word in a given string and returns the result as a dictionary.


sample input:
text = "The cat and the hat sat on the mat with another cat"

Sample Output:
{'the': 3, 'cat': 2, 'and': 1, 'hat': 1, 'sat': 1, 'on': 1, 'mat': 1, 'with': 1, 'another': 1}

"""
# SOLUTION

text=input("Enter a sentence:")
text=text.lower()
word=text.split()

freq={}
for w in word:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1

print(freq)