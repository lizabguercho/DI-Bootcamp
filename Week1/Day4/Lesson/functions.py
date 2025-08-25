#FUNCTIONS - reusable piece of code

#syntax

# def <name> ():
    #indented block of code
#    returned value

# def say_hello():
#     print("Hello, I am a function output")

# say_hello() # calling a function


# passing information to the function: argument -> always inside brackets
# def say_hello(language): #
#     if language == "PT":
#         print("Oi")
#     elif language == "HE":
#         print("שלום!")
#     else:
#         print("Hello")

# say_hello("HE")


# doc strings: documentation for the function

# def say_hello(language:str):
#     '''prints a greeting depending on a language argument''' #
#     if language == "PT":
#         print("Oi")
#     elif language == "HE":
#         print("שלום!")
#     else:
#         print("Hello")

# say_hello("HE")

# def say_hello_adv(language:str ="EN" ,name:str ="Bob"):
#     '''prints a greeting depending on a language argument''' #
#     if language == "PT":
#         print(f"Oi, {name}")
#     elif language == "HE":
#         print(f"שלום!,{name}")
#     elif language == "EN":
#         print(f"Hello, {name}")
#     else:
#         print(f"The language {language} is not suported")

# say_hello_adv()

#say_hello_adv()  -> we need to have default values in def function (language = "EN") if we are not passing any values in the calling part


# POITIONAL ARGUMENT    
def say_hello_adv(language:str ="EN" ,name:str ="Bob"):
    '''prints a greeting depending on a language argument''' #
    if language == "PT":
        print(f"Oi, {name}")
    elif language == "HE":
        print(f"שלום!,{name}")
    elif language == "EN":
        print(f"Hello, {name}")
    else:
        print(f"The language {language} is not suported")

# positional arguments : we pass only the value
say_hello_adv("Bob","PT")
# keywords arguments: we define to which arguments the value is related
say_hello_adv(name ="Bob",language ="PT")

# mixed positional and keyword argument: we can mix, but every positional argument needs to come first
# say_hello_adv ("Bob", language = "PT")
say_hello_adv("PT",name = "Sarah")

def country_info(country) -> str:
    if country == "Ukraine":
        capital = "Kyiv"
        # print(capital)
    elif country == "Naboo":
        capital = "Theed"
        # print(capital)
    elif country == "UK":
        capital = "London"
    else:
        print("This country is not supported")
    
    return capital

    
print(country_info("Ukraine")) # returns a str . If you return > 2 values, you return a tuple
ukraine_capital = country_info("Ukraine")
print(ukraine_capital) #-> output string

# return keyword: it return a value from the function

# scope
# local scope : scope inside (indentended after function def) the function
# we can NOT access a local variable on a global scope
# we only can access the variable on the local scope of a function if we usee the "return" keyword


#global scope: not in the scope of function(it is in the "main" file)
# we can access without modifying
# we can NOT modify it if we don't use a "global" keyword

bar_mizva = 13

def current_age():
    # age = 13
    # if age == bar_mizva:
    #     print("Mazal Tov!")
    global bar_mizva
    bar_mizva += 1

current_age()
print(bar_mizva)



