# LIST : A mutable sequence of elements 

my_list = ["Harry", "Ron", "Hermione", "Luna"]
my_list2 = list ("Harry")  # only 1 element can be

# print(my_list)
# print(my_list2)

# index: an index is a position  umber on the sequence and it start from 0

# print(my_list[1:4]) # slicing

# mutable 
my_list[2] = "Draco"
# print(my_list)
# print(len(my_list))
# List methods

fruits = ["apple", "mango", "kiwi", "lime", "mango"]
fruits.append("banana") #adds an element to the last index of the list
# print(fruits)
fruits.insert(1, "watermelon")
# print(fruits)
fruits.remove("mango") #removes only the first apperance
print(fruits)

fruits.pop()  # removes the last poition by default
print(fruits)

fruits.pop(2) # removes element by index 
print(fruits)


# excercise in class

list1 = [5, 10, 15, 20, 25, 50, 20]
my_index = list1.index(20)
list1[my_index] = 200
print(list1)

list1[list1.index(20)] = 200
print(list1)

#method to check after class:
# copy()
# extend()
# clear()
# sort() - sorts orginal list
# sorted() - creates a new list that is sorted
# count

print("hello")