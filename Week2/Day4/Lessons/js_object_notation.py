# import json
# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))


# my_family = {
#     "parents": ["Beth", "Jerry"],
#     "children": ["Summer", "Morty"]
# }

# # dump() and dumps()
# # convert a dictionary to a json file
# with open(f"{dir_path}//family.json","w", encoding = "utf-8") as f:
#     json.dump(my_family, f)

#  # to convert a dict in json string
# json_family = json.dumps(my_family)
# print(type(json_family))

# # load() - #taking from a file#   and loads() -# taking from a string#
# with open(f"{dir_path}//family.json","r", encoding = "utf-8") as f:
#     my_family2 = json.load(f)
#     print(type(my_family))

# # convert from json string to a dict
# parsed_family = json.loads(json_family)
# print(type(parsed_family))



# youtube video tutorial json

# 1. Load json file into python object

import json
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "0574893567",
            "emails":["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license" : false
        },
        {
            "name": "Jane Doe",
            "phone": "05356567",
            "emails": null,
            "has_license" : true         
        }
    ] 
        
}

'''

data = json.loads(people_string)
print(type(data["people"]))
print(data)

for person in data["people"]:
    print(person["name"])


# 2.  Dump a python object into json string

data = json.loads(people_string)


for person in data["people"]:
    del person['phone']

new_string = json.dumps(data, indent = 2, sort_keys = True)


print(new_string)
