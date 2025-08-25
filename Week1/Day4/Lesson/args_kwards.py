#*args = arguments (simple sequence structure like a list/set/tuple)
#**kwargs = ket word arguments (dictionary)

students = ["Harry", "Hermione", "Ron"]

def welcome(*args):
    if args:
        for arg in args:
            print(f"{arg}, Welcome to Hogwarts!")

welcome("Harry", "Hermione", "Ron")


def format_info(** kwargs):
    if kwargs:
        print(kwargs)
    if kwargs["parseltongue"]: 
        print(f"{kwargs["name"]} can talk to snakes")

format_info(name ="Harry", email = "harry@gmail.com", age = 14, parseltongue = True)
   
