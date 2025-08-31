
# DEQUE is optimized for fast appending and popping from both ends (left and right).
from collections import deque  
#initialization
list = ["a","b","c"]  
deq = deque(list)  
print(deq)  
deq.append("z")  # add on teh right side
deq.appendleft("g")  # add on the left side
print(deq)
deq.pop()  # remove from right side
deq.popleft()   # remove from right side
print(deq)


# Namedtuple()
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age')  
s1 = Student('Peter', 'James', '13')  
print(s1.fname) 


# ChainMap =combines a lot of dictionaries together and returns a list of dictionaries.
import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps) 

# OrderDict is a dictionary that ensures its order is maintained.
from collections import OrderedDict  
order = OrderedDict()  
order['a'] = 1  
order['b'] = 2  
order['c'] = 3  
print(order)  

#unordered dictionary
unordered=dict()
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)

# Infinite loops

#print the first four even numbers
# import itertools
# #This function takes in an iterable and goes over it indefinitely​.
# result = itertools.count(start = 0, step = 2)

# for number in result:
# # termination condition
#     if number < 8:
#         print (number)
#     else:
#         break

# print hello two times
import itertools

result = itertools.repeat('hello', times = 2)

for word in result:
    print (word)


# Finite iterators

import itertools

list_one = ['a', 'b', 'c']
list_two =['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)

for element in result:
  print (element)