"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
Write a function that takes a dictionary of student names and scores, and returns a list of names sorted by their scores.

sample input:
{"Akasha": 85, "Rahul": 90, "Priya": 78}

sample output:
['Priya', 'Akasha', 'Rahul']
"""
# SOLUTION

def sort_students_by_score(score):
    sorted_names = sorted(score, key=score.get)
    return sorted_names

students = {"Akasha": 85, "Rahul": 90, "Priya": 78}

print(sort_students_by_score(students))  

