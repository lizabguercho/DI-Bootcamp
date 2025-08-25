#Ex 1
def display_message():
    print("I am learning about functions in python")

display_message()

#Ex 2

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Game of Thrones")

# Ex 3
def describe_city(city, country:str = "Unknown"):
    print(f"{city} is in {country}")

#describe_city()  -> TypeError: describe_city() missing 1 required positional argument: 'city'
describe_city("Kyiv","Ukraine") 
describe_city("Kyiv")

# Ex 4

import random
def random_number (num):
    if num < 1 or num > 100:
        raise ValueError("Invalid number. Number must be between 1 and 100")
    rand_num = random.randint(1,100)
    if num == rand_num:
        print("Success!")
    else:
        print (f"Fail! Your number: {num}, Random number: {rand_num}")

random_number(50)

# Ex 5

def make_shirt(size,text):
    print(f"Shirt's size is {size} and it has a text: {text}")
make_shirt(36,"Be proud of yourself")

#modified version
def make_shirt(size = "Large",text = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt(size = "Medium")
make_shirt(size ="XS", text = "I love animals")
make_shirt(size="small", text="Hello!")

#Ex 6

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

show_magicians(magician_names)

def make_great(magician_names):
    for i,magician in enumerate(magician_names):
        magician_names[i] = f"The Great {magician}"
make_great(magician_names)
show_magicians(magician_names)
    
# Ex 7

def get_random_temp()->int :
    return random.randint(-10,40)

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {round(temp,2)} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16 :
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp <= 24 :
        print("Nice weather.")
    elif 24 <= temp < 32 :
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
    
main()

# bonus Floating-Point Temperatures
def get_random_temp()->float :
    return random.uniform(-10,40)

get_random_temp()
main()

# bonus Month-Based Seasons

def get_random_temp()->float :
    month = int(input("What month is right now?(1-12): "))
    if 1 <= month <= 3:
        temp = random.uniform(10,15)
    elif 4<= month <=6:
        temp = random.uniform(15,25)
    elif 7 <= month <= 9:
        temp = random.uniform(26,40)
    elif 10 <= month <= 12:
        temp = random.uniform(-10,10)
    return temp
main()

