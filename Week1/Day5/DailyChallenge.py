#Challenge 1
def sorting():
    words = input("Enter words (separated by ',' ): ")
    words_list = words.split(",")
    words_list.sort()
    updated_list = ",".join(words_list)
    print(updated_list)

sorting()

# Challenge 2
def longest_word(sentence):
    words = sentence.split()
    longest = " "
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))

