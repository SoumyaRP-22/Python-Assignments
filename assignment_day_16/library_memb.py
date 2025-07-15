class Book:
    def __init__(self,title,author):
        self.__title=title
        self.__author=author
        self.__is_borrowed=False
    
    def get_info(self):
        print(f"Title:{self.__title}, Author:{self.__author}")

    def borrow(self):
        self.__is_borrowed=True

    def is_borrowed(self):
        return self.__is_borrowed

# Part-1    
class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_genre(self):
        return self.genre

# Part-2
class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_subject(self):
        return self.subject


# Part-3
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def get_details(self):
        print(f"Member Name: {self.name}, ID: {self.member_id}")

fiction = FictionBook("Harry Potter", "J.K. Rowling", "Fantasy")
non_fiction = NonFictionBook("A Brief History of Time", "Stephen Hawking", "Science")
member = Member("Rahul", "M102")

# Book info before borrowing
print("Book Info Before Borrowing:")
fiction.get_info()
print("Borrowed:", fiction.is_borrowed())
non_fiction.get_info()
print("Borrowed:", non_fiction.is_borrowed())

fiction.borrow()
# Updated book statuses
print("\nBook Info After Borrowing Fiction Book:")
fiction.get_info()
print("Borrowed:", fiction.is_borrowed())
non_fiction.get_info()
print("Borrowed:", non_fiction.is_borrowed())

print("\nMember Details:")
member.get_details()