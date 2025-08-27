# Ex 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat1,cat2,cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    else:
        return cat3
        
            
cat1 = Cat("Puzya", 10)
cat2 = Cat("Bella", 5)
cat3 = Cat("Polly",2)  

oldest = find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {oldest.name} and it's age is {oldest.age}")

# Ex 2
class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        height_double = self.height * 2
        print(f"{self.name} jumps {height_double} cm high!")


davids_dog = Dog("Tobi", 60)
sarahs_dog = Dog("Motya", 15) 

print(davids_dog.name)
print(sarahs_dog.name)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
else:
    print("Sarah's dog is bigger")

# Ex 3

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
        

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
# Ex 4

class Zoo:
    def __init__(self,zoo_name,animals = None):
        self.zoo_name = zoo_name
        if animals is None:
            animals = []
        self.animals = animals
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the list")

    def get_animals(self):
        print(self.animals)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped= {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] =[]
            grouped[first_letter].append(animal)
        return grouped
    
    def get_groups(self):
        grouped = self.sort_animals()
        for letter,animal in grouped.items():
            print(f"{letter}:{animal}")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
print(brooklyn_safari.animals)
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
