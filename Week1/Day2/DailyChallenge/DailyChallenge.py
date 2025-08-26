#Challenge_1
number_input = int(input ("Type a number: "))
length_input = int(input ("Type a length: "))

multiple_list = []

for num in range(1,length_input+1):
    multiple_list.append(number_input*num)

print(multiple_list)


#Challenge_2

#option 1
user_string = input("Enter a string: ")
result = user_string[0]
for char in user_string[1:]:
    if char != result[-1]:
        result += char
print(result)

#option 2
user_string = input("Type a string: ")
if not user_string:
    print("")
result = []
last_checked = ""
for char in user_string:
    if char != last_checked:
        result.append(char)
        last_checked = char
print("".join(result))

# Happy bday Challenge

from datetime import date, datetime
user_bday = input("What is your birthdate? (DD/MM/YYYY): ")  #-> str
bday = datetime.strptime(user_bday, "%d/%m/%Y").date()
today = date.today() #-> date
age_in_days = (today - bday).days
age_in_years = age_in_days //365
print(f"{age_in_years} years")


cake = f"""
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

print(cake)



    
