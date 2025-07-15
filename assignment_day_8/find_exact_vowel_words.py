"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 3 **********************************

Problem statement: 
Write a function that takes a sentence as input and returns a list of all words that start and end with a vowel.

sample input:
Enter a sentence: apple banana orange avocado
Enter a sentence: umbrella igloo octopus
Enter a sentence: Anna and Eve are outside in India

sample output:
['apple', 'orange', 'avocado']
['umbrella', 'igloo', 'octopus']
['Anna', 'Eve', 'outside', 'in', 'India']
"""
# SOLUTION

def vowel_word(sentence):
    words=sentence.split()
    res=[]
    vowel='aeiouAEIOU'
    for word in words:
        if word[0] in vowel and word[-1] in vowel:
            res.append(word)
    return res

sentence=input('Enter a sentence:')
result=vowel_word(sentence)
print(result)