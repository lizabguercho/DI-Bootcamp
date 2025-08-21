# Challenge_1
number_input = int(input ("Type a number: "))
length_input = int(input ("Type a length: "))

multiple_list = []

for num in range(1,length_input+1):
    multiple_list.append(number_input*num)

print(multiple_list)


# Challenge_2

user_string = input("Type a string: ")
new_str = user_string[0]
for char in user_string[1:]:
    if char != new_str[-1]:
        new_str += char
print(new_str)





    
