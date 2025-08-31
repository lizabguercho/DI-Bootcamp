#ex 1
#Implement dunder methods for a Currency class to handle string representation,
#integer conversion, addition, and in-place addition.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount <= 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
        
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f"{self.amount} {self.currency}{ '' if self.amount <= 1 else 's'}"
    
    def __add__(self,other):
        if isinstance (other,Currency):
            if self.currency == other.currency:
                return int(self)+ int(other)
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif isinstance(other, (float,int)): 
                return int(self) + int(other)
    
    def __iadd__(self,other):
        self.amount = self + other
        return self
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)

#ex 3
#Goal: Generate a random string of length 5 using the string module.

import string
import random

def random_letters(length):
    all_letters = string.ascii_letters
    random_string =[]
    for i in range(length):
        random_string.append(random.choice(all_letters))
    updated_string = "".join(random_string)
    return updated_string

print(random_letters(5))

# ex 4

from datetime import date, datetime

today = date.today()
print(today)


# ex 5
today = datetime.today()
print(today)

new_year = datetime(2026, 1, 1)
print(new_year)

difference = new_year - today
print(difference)

# ex 6

def display_life_len(birth_date: str):
    b_day = datetime.strptime(birth_date,"%d-%m-%Y").date()
    today = date.today()
    life_len = today - b_day
    print(f"You lived {life_len.total_seconds()} seconds")

display_life_len("28-11-1993")

#ex 7

from faker import Faker
fake = Faker()
users = []

def add_users(num_users):
    for num in range(num_users):
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()    
        }
        users.append(user)

add_users(3)
print(users)