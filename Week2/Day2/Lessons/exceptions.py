print('Wrong string")
      
message = 'Python is fun'
print(message)

number = input('give me a number: ')
secret_number = 55

if number > secret_number:
    print('Congrats you won the guessing game')
else: 
    print('sorry, try again')

with try except block


secret_number = 55

while True:
    try:
        number = int(input('give me a number: '))
        if number > secret_number:
            print('Congrats you won the guessing game')
            break
        else:
            print(f'{number} is not the secret number: {secret_number}')
            break
    except Exception as e:
        print(e)
    finally:
        print('finally message')




def age():
    user_age = input("How old are you?\n>>> ")
    #######
    try:
        user_age = int(user_age)
        print("I AM AFTER USER_AGE")
    except:
        print("Your age is not a real age")
        user_age = 0
    #######
    print(f"Next year, you will be {user_age+1} years old")

age()

valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:
        userage = int(userage)
        valid_flag = True
    except:
        print("Please enter a real age")

print("Next year, your age will be",userage+1)

valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:
        userage    = int(userage)
        valid_flag = True
    except:
        pass

print("Next year, your age will be",userage+1)



#ex 1
def sum_numbers():
    my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
    total = 0
    for num in my_list:    
        try:
                total +=int(num)
        except ValueError:
            pass
    return total
    
print(sum_numbers())

#Else statement
valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:    # TRY THIS
        userage    = int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age!")
    else:   # ELSE
        valid_flag = True

#Finally

valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:    # TRY THIS
        userage    = int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age!")
    else:   # ELSE
        valid_flag = True
    finally:
        print('There may or may not have been an exception.')

print("Next year, your age will be",userage+1)