"""
************************* Python internship 2025 *****************************
************************* Assignment Day- 14 **********************************

Problem statement: 
Given a CSV file student_marks.csv, Read the file using pandas and perform the following tasks:

1. write a function to calculate the average marks for each student.
2. Write a function and use pandas to print names of students who scored more than 90 marks.

"""
import pandas as pd

df = pd.read_csv("assignment_day_14/student_marks.csv")

def calculate_average_marks(df):
    subjects = ['maths', 'science', 'computer', 'english']
    df['average'] = df[subjects].mean(axis=1)
    return df[['first_name', 'last_name', 'average']]

def print_high_scorers(df):
    subjects = ['maths', 'science', 'computer', 'english']
    high_scorers = df[df[subjects].gt(90).any(axis=1)]
    print("Students who scored above 90 in any subject:")
    for _, row in high_scorers.iterrows():
        print(f"{row['first_name']} {row['last_name']}")

averages = calculate_average_marks(df)
print("Average marks for each student:")
print(averages)

print()
print_high_scorers(df)
