# Challenge 1

words = input("Enter words (separated by ',' ): ")
words_list = words.split(",")
words_list.sort()
updated_list = ",".join(words_list)
print(updated_list)


