# Ex 1
user_input = input("Please, enter a single word(letters only): ")
if user_input.isalpha():
    print(f"You entered {user_input}")        
else:
    print("Invalid input.Please enter only letters")

result = {}
for i, letter in enumerate(user_input):
 
    if letter not in result:
        result[letter] = []
    result[letter].append(i)
   
# print(result)



#ex 2

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"

# # items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# # wallet = "$100"

# # items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# # wallet = "$1"

updated_wallet= int(wallet.strip("$"))

for key,value in items_purchase.items():
    updated_price = int(value.replace(",", "").strip("$"))
    items_purchase[key] = updated_price
print(items_purchase)

limit = updated_wallet
basket = []

for key,value in items_purchase.items():
  
    if value < limit:
        basket.append(key)
       

basket.sort()
print(basket)












