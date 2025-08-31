# Decorators are python  built in functions that we "apply" to our functions within the class, i.e methods

from datetime import datetime,date

class Person:
    def __init__(self, first_name, last_name,birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date =self. parse_birthdate(birth_date)
        self._email = None # protected attribute. set to None because it will come from the property (Incapsulation)
    # static method -decorator -  a method that doesn't really need the self. It will do change in the class.It's very small.
    @staticmethod
    def format_name(name):
        return name.capitalize()
    
    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str,"%d-%m-%Y").date()

    @classmethod  # method to be applied on the class
    def from_age(cls, first_name, last_name, age:int):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f"1-01-{birth_year}"
        return cls(first_name,last_name,birth_date)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    @ property

    def email(self):
        initial = self.first_name[0].lower()
        email = f"{initial}.{self.last_name.replace(" ", ".").lower()}@gmail.com"
        return email

########## DUNDER METHOD#########
    def __str__(self):
        return f"Hello! This is {self.first_name} {self.last_name}"    
    def __repr__(self):
        return f"{self.__dict__}"
    def __eq__(self,other):
        return self.last_name == other.last_name
    def __lt__(self,other):
        return self.age < other.age
    def __add__(self,other):
        return self.age + other.age
    

# to create object

p1 = Person("john", "snow da silva", "21-08-1990")
print(p1)
print(p1.birth_date)
print(p1.first_name)
# print(type(p1.birth_date))
print(p1.birth_date)
print(p1.age)
print(p1.email)

# How to use a class method when creating an object

p2 = Person.from_age("aria", "stark", 18)
p3 = Person.from_age("sansa", "stark", 21)
# print(p2 == p3)
# print(p2 < p3)
# print (p2 + p3)
# print(p2.birth_date)
# print(p2.email)
# # class ex


#serach for @property
# setter (p1.email= "the choosen" and the output should be "the.chooser@gmail.com") # put the different email which is not exactly formatted 
# getter : help to retieve the value
# deleter 


