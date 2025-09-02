import os
dir_path = os.path.dirname(os.path.realpath(__file__)) # this path will lead to a current file we are working with (it will find the closest folder.
# # always use it if you wnat to reach your file
# print(dir_path)
# # Python I/O

# #Old school syntax

# # try:
# #     f = open("secrets.txt")
# #     secret_data = f.read()
# #     print(secret_data)
# # except:
# #     raise ValueError
# # finally:
# #     f.close()


#Modern way
with open(f"{dir_path}/secrets.txt","a", encoding = "utf-8") as f:  # "r" -read, "w" -write, "a" -append
    file_content = f.read() #for read
    f.write("this is python file") #to overwrite
    f.write ('\nBla bla')   #to append with "a"
    print("content successfully added")

# #

# # read the file line by line
# with open(f"{dir_path}/star_wars.txt","r", encoding = "utf-8") as f:
#     # for line in f: to read line by line
#     #     print(f.readline())
#     # print ("end of document")

#     # print(f.readline(5)) # for reading first 5 characters
#     print(f.readlines()[4]) # for reading 9th line

# # readline()- singular = return one single line as a string.You can pass an argument  - a number for slicing this string
# # readlines() -plural = return a list where each element is a line of the document. YOu can pass an argument - a number for slicing the list.
    

# #Read all the file and return it as a list of strings. Then split each word into letters

# with open(f"{dir_path}/star_wars.txt","r", encoding = "utf-8") as f:
#     txt_content = f.readlines()
#     # final_list = []
#     # for line in txt_content:
#     #     final_list.append(list(line))

#     # list comprehension
#     #     
#     # print(final_list)
#     # final_list = [list(line) for line in txt_content]
#     # print(final_list)
    
# #Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

# with open(f"{dir_path}/star_wars.txt","r", encoding = "utf-8") as f:
#     txt_content  = f.readlines() # always creates list
   
#     clened_list = [line.strip() for line in txt_content]    
#     darth = clened_list.count("Darth")
#     luke = clened_list.count("Luke")
#     lea = clened_list.count("Lea")
#     print("darth", darth, "luke", luke, "lea", lea)

#Append your first name at the end of the file
# with open(f"{dir_path}/star_wars.txt","a", encoding = "utf-8") as f:
#     f.write("\nJuliana")

#Append "SkyWalker" next to each first name "Luke"
with open(f"{dir_path}/star_wars.txt","r", encoding = "utf-8") as f: # r+ for readinga and overwriting
    txt_content = f.readlines()
    skywalker = []
    
    for name in txt_content:
       
        if name == "Luke":
            skywalker.append(f"{name.strip()} Skywalker\n")
        else:
            skywalker.append(name)

   

with open(f"{dir_path}/star_wars.txt","w", encoding = "utf-8") as f:
    f.seek(0) # takes cursor to the beginning of the file
    f.writelines(skywalker)
    print("it was added")

