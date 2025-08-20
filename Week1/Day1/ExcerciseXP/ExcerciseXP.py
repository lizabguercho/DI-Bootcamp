# Ex.1
print("Hello world\n" *4)

# Ex.2
result = (99**3) * 8
print(result)

# Ex.3
# 5 < 3   -> False
# 3 == 3  -> True
# 3 == "3" -> False
# "3" > 3 -> False
# "Hello" == "hello"  -> False

# Ex.4
computer_brand = "Apple"
print(f"I have a {computer_brand} computer ")

# Ex.5
name = "Liza"
age = 31
shoe_size = 36
info = f"My name is {name} and I am {age} years old wearing shoe size {shoe_size}"
print(info)

# Ex.6
a = 6
b = 3
if a > b:
    print("Hello world")

#Ex.7
user_num = int(input("Give me a number"))
if user_num%2 == 0:
    print(f"{user_num} is even number")
else:
    print(f"{user_num} is odd")

# Ex.8
user_name = input("What is your name?")
computer_name = "Harry"
if user_name == computer_name:
    print("No way you have the same name!!!")
else:
    print("My name is more popular than yours haha")

# Ex.9
user_height = int(input("What is your height in cm?: "))
if user_height >= 145:
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")

