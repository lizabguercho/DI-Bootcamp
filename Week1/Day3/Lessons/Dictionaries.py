#DICTIONARIES = More complex data structures .It allows us to label the data inside structure

user_info = ["Juliana Schmidt", "juliana@gmail.com", 2435678, ("Ramat Gan","Sao Paulo")]
print(user_info)

user_info = {"full_name":"Juliana Schmidt",
             "email":"juliana@gmail.com",
             "score":2435678,
             "address": ("Ramat Gan","Sao Paulo")
             }


# Syntax : {"key":"value"}

# Accessing data inside a dictionary
print(user_info["email"])
print(user_info["address"][1])

# Adding key:value

user_info["family"]= ["Liza","Sam","Yeva"]
user_info.update({"hobbies":{"yoga","playstation","watercolor paint"}})
print(user_info)

# changing data inside dictionary

user_info["family"].append("john")
user_info["family"][1] = "Katty"
print(user_info)

# to change key but maintain a value
saved_value = user_info["score"]
del user_info["score"]
user_info["balance"] = saved_value
print(user_info)


# methods
print(user_info["email"].upper())
user_info["balance"] += 10000
print( user_info)

#ex in class

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]["student"]["marks"]["history"])
# history = sample_dict.get("history") doesn't work for nested dictionaries only for single one
print(user_info.get("balance"))


student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address' : 'Privet Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}


#LOOPS AND DICTIONARIES
#builtin method to help looping over
# keys() 
for key in student_info.keys():
    print(key)

# values()
for value in student_info.values():
    print(value)  

#items (both key:value) -> tuples

for key,value in student_info.items():
    print(key,value)  


#ex in class

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict)


grades = {
    "Mike":70,
    "Sarah" : 85,
    "Tom" : 90,
    "Anna" : 65,
    "Miriam": 50

}


for name, score in grades.items():
    if score >= 70:
        print(f"{name} passed exam,yay!")

# another very useul built-in methods
#
