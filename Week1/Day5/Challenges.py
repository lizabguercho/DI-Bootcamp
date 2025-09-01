#ex 1
fruits = ["apple", "orange","kiwi", "mango"]
fruits.insert(2,"cherry")
print(fruits)

# ex 2
my_string = "You are beautiful"
num_spaces = my_string.count(" ")
print(f"Number of spaces: {num_spaces}")

# ex 3

my_string_2 = "We have two daughters: Liza and Yeva"

lower_case_count = 0
for letter in my_string_2:
    if letter.islower():
        lower_case_count += 1

upper_case_count = 0
for letter in my_string_2:
    if letter.isupper():
        upper_case_count += 1        

print(lower_case_count)
print(upper_case_count)


# ex 4

def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(my_sum([1,5,4,2]))

# ex 5
def find_max(my_list):
    max_num = 0
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
print(find_max([0,1,3,50]))

# ex 6
# Write a function that returns factorial of a number

def factorial(num):
    if num < 0:
        raise ValueError ("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

print(factorial(4))
      
# ex 7

def list_count(lst,element):
    count = 0
   
    for item in lst:
        if item == element:
            count += 1
    return count

print(list_count(['a','a','t','o'],'a'))


# ex 8

#Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
import math
def norm(lst1):
    result_sum = 0
    for i in lst1:
        result_sum += i**2
    squre_root_sum = math.sqrt(result_sum)

    return int(squre_root_sum)

print(norm([1,2,2]))

# ex 9
def is_mono(lst2):
     # check if non-decreasing
    increasing =True
    for i in range(len(lst2) - 1):
        if lst2[i] > lst2[i+1]:
            increasing = False
            break
      # check if non-increasing       
    decreasing = True
    for i in range(len(lst2) - 1):
        if lst2[i] < lst2[i+1]:
            decreasing = False
    return increasing or decreasing
        
print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# ex 10

#Write a function that prints the longest word in a list.

def longest_word(lst3):
    longest_word = ""
    for item in lst3:
        if len(item) > len(longest_word):
            longest_word = item
    return longest_word

print(longest_word (["apple", "beautiful", "dog"]))

def longest_word(lst3):
    return max(lst3, key=len)

print(longest_word(["apple", "beautiful", "dog"]))  

# ex 11

def separate_int_str(lst4):
    digit_list = []
    str_list = []
    for item in lst4:
        if isinstance(item,int):
            digit_list.append(item)
        else:
            str_list.append(item)
    return digit_list, str_list

lst4 = ["mother", 4,16, "dog", "f"]
print(separate_int_str(lst4))

# ex 12

def is_palindrome(str1):
    return str1 == str1[::-1]

print(is_palindrome('radar'))
print(is_palindrome('John'))

# ex 13

def sum_over_k (sentence,k):
    words_list = sentence.split()
    words_count = 0
    for word in words_list:
        if len(word) > k:
            words_count += 1
    return words_count

sentence = 'Do or do not there is no try'    
k=2
print(sum_over_k(sentence,k))

def sum_over_k(sentence, k):
    return sum(1 for word in sentence.split() if len(word) > k)

# ex 14

def dict_avg(dict1):
    sum_value = 0
    for value in dict1.values():
        sum_value +=value
    average_value = sum_value/len(dict1)
    return average_value

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))


# ex 15

def common_div(num1,num2):
    divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return divisors
    

print(common_div(10,20))

# ex 17
def weird_print(lst5):
    for i in range(len(lst5)):
        if i % 2 == 0 and lst5[i] % 2 == 0:
            print(lst5[i])
    

weird_print([1,2,2,3,4,5])

# ex 18
def type_count(**kwargs):
    type_dict = {}
    
    for key,value in kwargs.items():
        value_type = type(value)
        if type_dict[value_type] = 1
        print()
    
   

type(type_count(a=1,b='string',c=1.0,d=True,e=False))
    

            





