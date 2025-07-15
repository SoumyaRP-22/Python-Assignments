from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,email):
        self.__name=name
        self.__email=email
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email=email

    @abstractmethod
    def display_details(self):
        pass

class Student(Person):
    def __init__(self, name, email, roll_no):
        super().__init__(name, email)
        self.__roll_no=roll_no
    def get_roll_no(self):
        return self.__roll_no
    def set_roll_no(self,roll_no):
        self.__roll_no=roll_no

    def display_details(self):
        print(f"Name:{self.get_name()}, Email:{self.get_email()}, Roll no:{self.get_roll_no()}")

class Professor(Person):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id=employee_id
    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id
    
    def display_details(self):
        print(f"Name:{self.get_name()}, Email:{self.get_email()}, Employee Id:{self.get_employee_id()}")

class Course:
    def __init__(self, course_code, title):
        self.__course_code = course_code
        self.__title = title
        self.__students = []
        self.__professor = None

    def get_course_code(self):
        return self.__course_code

    def set_course_code(self, code):
        self.__course_code = code

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_students(self):
        return self.__students

    def get_professor(self):
        return self.__professor

    def add_student(self, student):
        self.__students.append(student)

    def assign_professor(self, professor):
        self.__professor = professor

    def get_course_summary(self):
        print(f"Course Code: {self.__course_code}")
        print(f"Title: {self.__title}")
        print("Professor: ", end="")
        if self.__professor:
            self.__professor.display_details()
        else:
            print("Not assigned")
        print("Enrolled Students:")
        if self.__students:
            for student in self.__students:
                student.display_details()
        else:
            print("No students enrolled.")

class Department:
    def __init__(self, name):
        self._name = name 
        self._courses = []

    def add_course(self, course):
        self._courses.append(course)

    def list_courses(self):
        print(f"Courses in {self._name} Department:")
        for course in self._courses:
            print(f"{course.get_course_code()}: {course.get_title()}")

if __name__ == "__main__":
    cs_dept = Department("Computer Science")

    s1 = Student("Alice", "alice@example.com", "CS101")
    s2 = Student("Bob", "bob@example.com", "CS102")
    p1 = Professor("Dr. Smith", "smith@example.com", "EMP987")

    course = Course("CS200", "Data Structures")
    cs_dept.add_course(course)

    course.assign_professor(p1)
    course.add_student(s1)
    course.add_student(s2)

    course.get_course_summary()