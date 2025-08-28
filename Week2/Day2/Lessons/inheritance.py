#OOP - Inheritance

class Animal: # parent class
    def __init__(self,name,family,legs):
        self.name = name
        self.family = family
        self.legs = legs
    def sleep(self):
        return f"{self.name} is sleeping (parent class)"
        
    def run(self):
        return f"{self.name} is running"
    
class Dog(Animal): # child class -> inheritance from Animal (parent) class

    def __init__(self,name,family,legs,age,trained):
        super().__init__(name,family,legs) # to take attributes from parent
        self.age = age
        self.trained = trained

    def sleep(self):
        return f"{self.name} is sleeping (child class)"

    def fetch_ball(self):  # if we have def here it will not be used in parent class (only in child)
        return f"{self.name} is running for the ball"

class DogPet(Dog): # also inherets from Animal
    pass

class Cat(Animal):

    def sleep(self):
        base_msg = super().sleep()
        return f"{base_msg} on the roof"
        
class Alien():
    def __init__(self,planet,superpower):
        self.planet =planet
        self.superpower =superpower

    def fly(self):
        return f"{self.name} is flying"
    
    def sleep(self):
        return f"{self.name} is sleeping (parent class)"

#Miltiple Inheritence
class AlienDog(Alien,Dog):
    def __init__(self,name, family, legs, age, trained, planet, superpower):
        Alien.__init__(self, planet, superpower)
        Dog.__init__(self, name, family, legs, age, trained)
    pass









dog1 = Dog("Tobi","Canine", 4, 10, True)
print(dog1.legs)
dog1.sleep()
dog1.fetch_ball()
cat1 = Cat("Lola","Felidae",4)
print(cat1.sleep())
# horse1 = Animal("Spirit", "Equidae", 4)
# horse1.fetch_ball()

my_pet = DogPet("Motya","Canine",4,5,False)
print(my_pet.run())

alien_dog1 = AlienDog("Xuxa", "Canine", 6, 523, True, "Jupiter", True)
print(alien_dog1.fly())
print(alien_dog1.fetch_ball())
print(alien_dog1.run())
print(alien_dog1.sleep())