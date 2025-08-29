#ex 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

bengal_obj = Cat("Shy", 4)
chartreux_obj = Cat("Lora", 12)
siamese_obj = Cat("Pinky", 6)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()


#Ex 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
       return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/ self.age * 10
        

    def fight(self, other_dog):
        power1 = self.run_speed() * self.weight
        power2 = other_dog.run_speed() * other_dog.weight

        if power1 > power2:
            return f"{self.name} won this fight"
        elif power1 < power2:
            return f"{other_dog.name} won this fight"
        else:
            return f" The fight between {self.name} and {other_dog.name} finished in a tie"
        
dog1 = Dog("Tobi", 4 , 50)
dog2 = Dog("Luna",7 , 18)

print(dog1.bark())
print(dog2.bark())
print(dog1.run_speed())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog1))

#ex 4

class Person:
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    
    def is_18(self) -> bool:
        '''Return True if the preson is 18,otherwise False'''
        return self.age  >= 18
        

class Family():
    def __init__(self, last_name):
        self.last_name = last_name
        self.members =[]
        
    def born(self, first_name, age):
        '''Creates a new person with first name and age and adds them to members list'''
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)
      

    def check_majority(self,first_name):
        '''Check if person exists in the family and is 18 or older'''
        for member in self.members:
             if member.first_name == first_name and member.is_18():
                print(f"You are over 18, your parents accept that you will go out with your friends")
                return
        print("Sorry, you are not allowed to go out with your friends.")
                
                         
    def family_presentation(self):
        ''' prints the family's last name and all members'''
        print(f"Family {self.last_name}: ")
        for member in self.members:
            print(f"- {member.first_name} {member.last_name}, {member.age} years old")

smiths = Family("Smith")
smiths.born("Katty",32)
smiths.born("Bob",40)
smiths.born("Ally",5)

smiths.family_presentation()
smiths.check_majority("Katty")
smiths.check_majority("Bob")
smiths.check_majority("Ally")