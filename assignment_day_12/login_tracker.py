"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 12 **********************************

Problem statement: 
You are given a list of login logs in the format (username, timestamp). 
Write a function to return the most recent login timestamp for each user.


sample input:
logs = [
  ("alice", 1623),
  ("bob", 1610),
  ("alice", 1629),
  ("bob", 1640)
]

sample output:
{'alice': 1629, 'bob': 1640}
"""
# SOLUTION

def login_tracker(logs):
    logins={}
    for username,timestamp in logs:
        if username not in logins or timestamp > logins[username]:
            logins[username]=timestamp
    return logins

logs = [
  ("alice", 1623),
  ("bob", 1610),
  ("alice", 1629),
  ("bob", 1640)
]
print(login_tracker(logs))