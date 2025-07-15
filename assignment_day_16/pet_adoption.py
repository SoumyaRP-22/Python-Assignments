# Part-1
class Pet:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__adopted = False

    def get_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def adopt_pet(self):
        self.__adopted = True

    def is_adopted(self):
        return self.__adopted


# Part-2
class Dog(Pet):
    def bark(self):
        print("Woof!")


class Cat(Pet):
    def meow(self):
        print("Meow!")


# Part-3
class Person:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def get_details(self):
        print(f"Name: {self.name}, Phone: {self.phone_number}")


# Part-4
dog = Dog("Buddy", 3)
cat = Cat("Luna", 2)

person = Person("Anita", "999999210")

print("Pet Info:")
dog.get_info()
cat.get_info()

dog.adopt_pet()
# Adoption status
print("\nAdoption Status:")
print("Dog adopted:", dog.is_adopted())
print("Cat adopted:", cat.is_adopted())
