#Ex 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys,values))
print(new_dict)


# #Ex 2
total_cost = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for name, age in family.items():
    if age < 3:
         print(f"{name}: 0$")
    elif 3 <= age <= 12:
        total_cost += 10
        print(f"{name}: 10$")
    elif age > 12:
        total_cost += 15
        print(f"{name}: 15$")
print(f"Total cost of tickets: {total_cost}$")

# Bonus
total_cost = 0
member_info = {}
while True:    
    name = input("Enter your name (or 'q' to quit): ")
    if name =="q":
        break
    try:
        age =int(input("Enter your age: "))
        member_info[name] = age
    except ValueError:
        print("Invalid age.Please enter number")
print(member_info)
    
for name, age in member_info.items():
    if age < 3:
         print(f"{name}: 0$")
    elif 3 <= age <= 12:
        total_cost += 10
        print(f"{name}: 10$")
    elif age > 12:
        total_cost += 15
        print(f"{name}: 15$")
print(f"Total cost of tickets: {total_cost}$")


# ex 3

brand = {}
brand["name"] = "Zara"
brand["creation_date"] = 1975
brand["creator_name"] = "Amancio Ortega Gaona"
brand["type_of_clothes"] =["men", "women", "children", "home"]
brand["international_competitors"] = ["Gap", "H&M", "Benetton"]
brand["number_stores"] = 7000
brand["major_colors"] ={
    "France":"blue",
    "Spain":"red",
    "US" :["pink","green"]
}

brand['number_stores'] = 2 #Change the value of number_stores to 2.
clients = ",".join(brand["type_of_clothes"])
print(f"Zara's clients can buy things in 4 different departments: {clients}") #Print a sentence describing Zara’s clients using the type_of_clothes key.
brand["country_creation"] = "Spain" #Add a new key country_creation with the value Spain.

if "international_competitors" in brand.keys(): #Check if international_competitors exists and, if so, add “Desigual” to the list.
    brand["international_competitors"].append("Desigual")

del brand["creation_date"] #Delete the creation_date key.

print(brand["international_competitors"][-1]) #Print the last item in international_competitors.

print(brand["major_colors"]["US"]) #Print the major colors in the US.
print(f"The major colors of US are {" and ".join(brand["major_colors"]["US"])}")
print(len(brand))  #Print the number of keys in the dictionary.

print(list(brand.keys())) #Print all keys of the dictionary.

# ex 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1 Create a dictionary that maps characters to their indices:
dict_1 = {}
for i, name in enumerate(users):
    dict_1[name] = i

#2  Create a dictionary that maps indices to characters:
dict_2 = {}
dict_2 = dict(enumerate(users))
print(dict_2)

#3 Create a dictionary where characters are sorted alphabetically and mapped to their indices:
dict_3 = {}
sorted_by_name = sorted(users)
for i, name in enumerate(sorted_by_name):
    dict_3[name] = i
print(dict_3)



