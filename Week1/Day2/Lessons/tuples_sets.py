# #tuples : Immutable and ordered
# numbers = (10,20,30,40,50,20)
# # numbers2 = tuple(10) #can't be created from 1 element
# numbers2 = tuple(numbers) # needs to have a sequence in the argument
# print(numbers2)
# #number2[1] =200  # error because tuples are immuatable
# print(numbers[1])  # can use index because tuple is ordered

# #methods

# # print(numbers.count(20))
# # print(numbers.index(20)) # first occurance

# # concatenate tuples

# fruits = ("apple", "mango", "kiwi", "lime", "mango")
# vegs = ("tomato", "potato", "lettuce")
# fruits_vegs = fruits+vegs
# # print(fruits_vegs)

# # a,b,c,d,e,f = numbers
# # print(a)
# # print(b)
# # print(c)
# # print(d)


# #SETS = unordered (no index) sequence not duplicated  removes duplicates automatically
# my_set = {1,4,8,9}
# my_set2 = set(my_set)
# print(my_set,my_set2)

# my_set.add(55)
# print(my_set)
# user_names = ["juli", "john", "juli","bob","mark", "john"]
# t_user_names = set(user_names)
# clean_user_names = list(t_user_names)
# print(clean_user_names)


# names = {"Juliana","Israel","Dina"}
# countries = {"USA","Brazil","Israel"}
# print(names.intersection(countries)) # to find same things in sets
# print(names.difference(countries))
# print(countries.difference(names)) # to find diffrences between sets

# excercise in class
my_fav_colors = {"blue", "purple","green","yellow", "black"}
friends_fav_colors = {"white", "blue", "orange", "green","pink"}

my_fav_colors.add("grey")
print(my_fav_colors)
print(my_fav_colors.intersection(friends_fav_colors))
my_fav_colors.clear()
print(my_fav_colors)

