# CONDITIONALS

#SYNTAX

# if <condition>:
    #<action>

# if 5 < 3:
#     print("Hello there!")


# user_num = int(input("Guess a number"))
# secret_num = 18

# if user_num == secret_num:
#     print("Congrats, you won!")
# elif  user_num == 7:
#     print("That's my lucky number!")



# user_name = input("What is your name? ")
# if len(user_name) <= 5:
#     print("You have a short name :)")
# else:
#     print("You have a long name")

# my_hobbies = "sport, code, food, icecreams, netflix"
# if "yoga" in my_hobbies or "soccer" in my_hobbies:
#     print("Let's have a pizza")


# Excercise in class
user_number = int(input("Give me a number from 1 to 100 "))
if user_number% 3 == 0 and user_number%5 == 0:
    print("FizzBuzz")
elif user_number%3 == 0:
    print("Fizz")
else:
    print("Buzz")