MATRIX_STR = '''7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

matrix = []
for line in MATRIX_STR.splitlines():
    matrix.append([char for char in line])

decoded_message = ""
for col_index in range(len(matrix[0])):
    for row in matrix:
        char = row[col_index]
        if char.isalpha():
            decoded_message += char
        else:
            decoded_message += " "
        
print(decoded_message.strip())


    





