# OOP: Object oriented programming
#CLASS = blueprint of the object where we will define what are the properties and behaviors of the object

# Class:a structure that defines the properties and behaviors of the objects.
#



#syntax

class Dog: # class needs to start with  acpital "D"
    #the constructir function (all properties)
    # self is the internal dictionary that has the properties from the class
    #self  -> {bread: -----, nickname:-------,color:------}
    def __init__(self,breed:str, nickname:str, color:str, age:int = None,is_trained = False):  # it will be called automatically when we create an object .Always self at the beginning.
        print("object was created")
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.age = age
        self.is_trained = is_trained
        if age == None:
            self.dogs_years_age = None
        else:
            self.dogs_years_age = age * 7
       
        
    ############## Methods = behavior of the object ##################
    def bark(self):
        print(f"{self.nickname} is barking")
    def sit(self):
        if self.is_trained:
            print(f"{self.nickname} is sitting")
        else:
            print(f"{self.nickname} is not trained")
    def rename(self,new_name):
        self.nickname = new_name
        return self

# create an object from the class Dog: (not in the scope of class (out of def))

dog1 = Dog("chowchow", "lion", "orange", 5)
dog2 = Dog("collie", "laddy", "beige and white", 15, True)
# create a specific attribute for dog2
dog2.is_service_dog = True

print(dog1.color) # to access atributes of the object we use dot notation "."
print(dog1.__dict__)
print(dog2.__dict__)



############## Methods = behavior of the object ##################

dog3 = Dog("Labrador", "Rex", "golden", 7, True)
dog3.bark() # calling the metho of object (MORE COMMON)
Dog.bark(dog3) # calling the method on the class and pass the object as an argument
dog3.sit()
dog1.sit()
dog1.rename("liza")
print(dog1.nickname)

my_dogs = [dog1,dog2,dog3]
for dog in my_dogs:
    print(dog.nickname)

print(type(dog3))

class Dog():

    # Initializer / Instance Attributes
    def __init__(self):
        print("A new dog has been initialized !")

shelter_dog = Dog()

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)

shelter_dog = Dog(name_of_the_dog="Rex")
# or
shelter_dog = Dog("Rex")

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

shelter_dog = Dog('Rex')
other_shelter_dog = Dog("Jimmy")

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

first_person = Person("John", 36)

print(first_person.name)
print(first_person.age)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks ! WAF")
shelter_dog = Dog("Rex")
shelter_dog.bark()

# two arguments on def()
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

shelter_dog = Dog("Rex")
shelter_dog.bark()
shelter_dog.walk(10)


# rename method
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

shelter_dog = Dog("Rex")
shelter_dog.rename("Paul")

print(shelter_dog.name)


# class ex

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)
    def rename(self,new_name):
        self.name = new_name

first_person = Person("John", 36)
first_person.show_details()
first_person.rename("Bob")
print(first_person.name)
first_person.show_details()

# class ex
class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

# class ex

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)