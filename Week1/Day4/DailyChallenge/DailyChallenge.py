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

result = ""
for col_index in range(len(matrix[0])):
    for row in matrix:
        char = row[col_index]
        if char.isalpha():
            result += char
        else:
            result += " "
        
print(result.strip())


    





