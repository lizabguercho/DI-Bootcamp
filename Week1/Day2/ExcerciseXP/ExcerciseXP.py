# ex 1

my_fav_numbers = {1,3,6,8,7}   ""
friend_fav_numbers = {3,4,7,5,9}

my_fav_numbers.add(11)
my_fav_numbers.add(23)
my_fav_numbers.remove(11)
my_fav_numbers.remove(23)
our_favorite_numbers =my_fav_numbers.union(friend_fav_numbers)
print(my_fav_numbers)
print(our_favorite_numbers)

# ex 2

#We can't add integers to a tuple of integers because tuples are immutable. If we really want to that, we can convert a tuple to list, add an integer and then convert it to a tuple again.

#ex 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# ex 4
Float is a decimal number and integer is a whole number
num_list = [1.5]

for num in range (1,8):
    last_number = num_list[-1]
    num_list.append( last_number + 0.5)
print(num_list)
    

#ex 5

for i in range (1,21):
    print(i)

numbers = []  
for i in range(1,21):
    numbers.append(i)

for i in numbers:
    if numbers.index(i) % 2 == 0:
        print(i)

# ex 6
my_name = "Harry"
user_name =input("Enter your name: ")

while user_name != my_name:
    user_name =input("Enter your name: ")
   
# # ex 7

user_fav_fruits = list(input("Write down your favorite fruits (separated by spaces):"))
any_fruit = input("Write down a name of any fruit:")
if any_fruit in user_fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# ex 8

toppings = []
while True:
    topping = input("enter the topping you want on your pizza, or q for quit:")
    if topping == "q":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + len(toppings)* 2.50

print(toppings)
print(str(total_cost) + "$")

#ex 9
total_cost = 0
while True:
    user_age = int(input("Write down your age:(enter 0 to quit) "))  
    if user_age == 0:
        break      
    elif user_age < 3:
        total_cost += 0
    elif 3 <= user_age <= 12:
        total_cost += 10
    else:
        total_cost += 12

print(str(total_cost) + "$")


# Ex 10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

finished_sandwiches = []

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(sandwich_orders)

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
    
