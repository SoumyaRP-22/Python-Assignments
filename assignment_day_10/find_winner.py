"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 10 **********************************

Problem statement: 
You are given a list of votes (each vote is represented by a candidate's name). 
Each element in the list represents a vote cast for a candidate.
Write a Python function to determine the winner, i.e., the candidate who received the most votes.

sample input:
votes = [
    "Alice",
    "Bob",
    "Alice",
    "Charlie",
    "Bob",
    "Alice"
]

sample output:
Alice # because she received the most votes
"""
# SOLUTION

def winner(votes):
    count = {}
    
    for candidate in votes:
        if candidate in count:
            count[candidate] += 1
        else:
            count[candidate] = 1
    
    max_votes = 0
    winner = None
    for candidate, count in count.items():
        if count > max_votes:
            max_votes = count
            winner = candidate
            
    return winner

votes = [
    "Alice",
    "Bob",
    "Alice",
    "Charlie",
    "Bob",
    "Alice"
]

print(winner(votes))
