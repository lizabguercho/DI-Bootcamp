
while True:
    user_input = input("Write down a string: ")
    length_str = len(user_input)
    if length_str < 10:
        print("String not long enough.")
    elif length_str > 10:
        print("String too long.")
    else:
        print("Perfect string 😍")
        print(f"First character is {user_input[0]} and last character is {user_input[-1]}")
        break
print()
for i in range(1,length_str+1):
    print(user_input[:i])

print()

import random
char_list = list(user_input)
random.shuffle(char_list)
shuffle_string = "".join(char_list)
print(f"Shuffled string : {shuffle_string}")

