import os
from anagram_checker import AnagramChecker

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path =os.path.join(dir_path,'sowpods.txt')
checker = AnagramChecker(file_path=file_path)

print("**************************")
print("WELCOME TO ANAGRAM CHECKER")
print("**************************")


def is_a_single_word(word, ascii_only = True):
    word = word.strip()
    if not word:
        return False, "Empty input. Please type a word."
    parts = word.split()
    if len(parts) != 1:
          return False, "Only a single word is allowed (no spaces)."
    
    word = parts[0]

    if ascii_only:
          if not word.isascii() or not word.isalpha():
            return False, "Only letters A-Z are allowed (no digits or symbols)."

    return True, "ok"

while True:
    print("----Menu----")
    print("1. Input a word")
    print("2. Exit (2 for quit)")
    
    choice = input("Choose (1-2): ").strip()
    
    if choice == "1":
        word = input("Enter a word:").strip()
        if not word:
            print("Please type something")
            continue
        try:
            is_valid, reason = is_a_single_word(word)
            if is_valid and checker.is_valid_word(word):
                print(f"'{word}' is a valid English word.")
                anagrams = checker.get_anagrams(word)
                print(f"Anagrams for your word:{', '.join(anagrams)}")
            
            else:
                print(f"'{word}' is NOT a valid English word - {reason}")
            
        except Exception as e:
                print(f"Validation error: {e}")
    elif choice == "2":
        print ("Good bye!")
        break
    else:
         print("Invalid choice. Please select 1 or 2.")

       
            

