from ExcerciseXP import Dog
import random
class PetDog(Dog):
    def __init__(self,name, age, weight, trained):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play (self,*args):
        all_names = [self.name] + list(args)
        if len(all_names) == 1:
            names_str = all_names[0]
        else:
            name_str = ", ".join(all_names[:-1]) + " and " + all_names[-1]
        return f"{name_str} all play together"

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
    
my_dog = PetDog("Motya", 10, 2, True)
my_dog.train()
print(my_dog.play("Buddy", "Max"))
my_dog.do_a_trick()