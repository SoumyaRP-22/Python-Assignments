"""
************************* Python internship 2025 *****************************
************************* Assignment Day- x **********************************

Problem statement: 
Create a class called Student with the following requirements:
- data members (attributes) (Initialized using __init__)
    name (str)
    roll_no (int)
    marks (dict): A dictionary where keys are subject names and values are marks (e.g., {"Math": 85, "English": 78})

    
- Methods to Implement
    1. display_info(self): Prints the student's name and roll number.
    2. add_mark(self, subject: str, mark: int): Adds or updates the mark for a given subject.
    3. calculate_average(self): Returns the average of all subject marks.
    4. get_grade(self): Returns the grade based on the average mark:
        90+ → "A"
        75-89 → "B"
        60-74 → "C"
        Below 60 → "D"
"""
# SOLUTION

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Student's name: {self.name}")
        print(f"roll no.: {self.roll_no}")

    def add_mark(self, subject, mark):
        self.marks[subject] = mark
        print(f"Mark updated for {subject}: {mark}")

    def calculate_average(self):
        total = sum(self.marks.values())
        average = total / len(self.marks)
        return average
    
    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "D"

# Create students
student1 = Student("Subham", 201, {"Math": 95, "Science": 91, "English": 88})
student2 = Student("Aditi", 202, {"Math": 72, "History": 69, "English": 65})
student3 = Student("Rohan", 203, {"Math": 59, "Biology": 55, "Geography": 62})
student4 = Student("Nidhi", 204, {"Physics": 84, "Chemistry": 89, "Math": 78})
student5 = Student("Sushil", 205, {"English": 45, "Math": 52, "Economics": 49})

# List of students
students = [student1, student2, student3, student4, student5]

# Add or update marks
student1.add_mark("Computer", 93)
student2.add_mark("Science", 74)
student3.add_mark("English", 58)
student4.add_mark("Biology", 90)
student5.add_mark("History", 60)

# Display student info with average and grade
for student in students:
    student.display_info()
    print("Marks:", student.marks)
    print(f"Average: {student.calculate_average():.2f}")
    print(f"Grade: {student.get_grade()}")
    print("-" * 30)