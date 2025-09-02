
# # ex 1
import os
import random
dir_path = os.path.dirname(os.path.realpath(__file__)) 

def get_words_from_file(file_path):
    words = []
    with open(f"{file_path}/words.txt","r", encoding = "utf-8") as f:
        for line in f:
            words.extend(line.split())

        return words

file_path = os.path.join(dir_path)
print(get_words_from_file(file_path))

def get_random_sentence(length):
    words_list = get_words_from_file(file_path)
    result = []
    for _ in range(length):
        result.append(random.choice(words_list))
    
    sentence = " ".join(result)
    return sentence.lower() + "."

def main():
    print("This program generates a random sentence from your desired length input")

    user_input = input("Enter desired length of a sentence (between 2 and 20): ")
    try:
        length = int(user_input)
    except ValueError:
        print("Not valid input. Please, enter a number")
        return

    if 2<= length <= 20:
        sentence = get_random_sentence(length)
        print("Here is your random sentence")
        print(sentence)
    else:
        print("Error: The number must be between 2 and 20")  

if __name__ == "__main__":
    main()
 
        
#ex 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
"""
# Load JSON string
data = json.loads(sampleJson)
# to access salary
print("Salary: ", data["company"]["employee"]["payable"]["salary"])

# add birth_date
data["company"]["employee"]["birth_date"] = "YYYY-MM-DD"
print(data)
data["company"]["employee"]["birth_date"] = "1993-26-05"
print(data)
# save modified JSON to a file
with open(f"{dir_path}/modified.json","w", encoding = "utf-8") as f: 
    json.dump(data, f, indent = 2)

print("Modified json saved to modified.json")