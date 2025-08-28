class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)

class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()

my_instance_2 = ChildClass()
my_instance_2.func()


#We can restrict access to methods and variables. 
# This prevents data from direct modification, which is called encapsulation. 
# In Python, we denote private attributes using underscore as prefix i.e., single _ or double __.
#Lets define an object class Computer and try to access its variables and methods both private and global.

class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell() # public function
# c.__sell() # gives an error :'Computer' object has no attribute '__sell'( because it's a private function (__sell))

# Setter function to change a private function
# change the price
# c.__max_price = 1000
# c.sell()
# >> The private attribute __max_price cannot be changed
# >> Selling Price: 900

# using setter function
# c.set_max_price(1000)
# c.sell()
# >> Selling Price: 1000

class Parrot():

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
# >> Parrot can fly

flying_test(peggy)
# >> Penguin can't fly


class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis() 

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)