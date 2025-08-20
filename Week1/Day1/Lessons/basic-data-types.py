# # Basic value types

# # Strings

# my_name = "Liza"

# print(len(my_name))

# #access chars by index
# print(my_name[2])

# #they are immutable we can't change letter instead of each other
# #my_name[0] = "G" # can't do that

# #string functions/method

# print(my_name.lower())
# print(my_name.upper())
# print(my_name.capitalize()) #just the first letter to be capital
# print(my_name.title()) # capitalize first letter of each word


# student = "Harry Potter"
# student_2 = student.replace("Harry", "Ginny") # to change words and letters 
# print(student_2)

# price = "15$"
# clean_price = price.strip("$")  # strip(arg) deletes str from both sides;  strip() without argument it will delete spaces
# print(clean_price) 

#excercise in class
# description = "strings are"
# print(description.upper())
# description2 = description.replace("are", "is")
# print(description2)
# print(description[:7])


#Numbers
# # integers (int)
# age = 35
# age += 1 # increment
# print(age+5)
# print(7 +(-2))
# print(10/2)  # division will always give a float 5.00 (way of creating a float)
# print(10%2) # module gives you a remainder

# #floats
# print(3.5 + 3)
# print((10/3))
# division =10/3
# print(round(division,2))

# # Type casting

# age = int(input("How old are you?" ))
# # print(type(age))

# # print(age +10)

# height = float(input("What is your height?"))
# print(type(height))

# age = str(age)
# print(type(age))


# Booleans (True and False)

print(5>7)
print(-1 != 1)


# General Useful Knowledge

#Addin types
my_string = "Hello World "

python = "Python is fun"

print (my_string + python)

print("Hello, aren't you having fun?\n" * 5) # \n go to a next line

# Hello, aren't you having fun?
# Hello, aren't you having fun?
# Hello, aren't you having fun?
# Hello, aren't you having fun?



# print('Hello, aren\'t you having fun?\n' * 5)

# print("Hello, aren't you having fun?\t" * 5)  # tab space between strings

# # f' string

# user_name = input ('What\'s your name?')
# print(f'Welcome, {user_name}!')

first_name = "Liza"
last_name = "Benguerchon"

print(f"{first_name} {last_name}")


