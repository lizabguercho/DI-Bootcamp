# other very useful built-in methods

# enumerate() -> Aloows us to access index and the element of a sequence

students = ["Harry", "Ron","Hermione","Draco","Luna"]

for i, name in enumerate(students):
    students[i] = f"Welcome {name}"
print(students)


# zip()

scores = [100,87,4938,60,89]
students = ["Harry", "Ron","Hermione","Draco","Luna","Langbotton"]

students_grades = dict(zip(students,scores))
print(students_grades)

# list comprehension
numbers = list(range(1,11))
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

squared_numbers = [num**2 for num in numbers if num%2 == 0]
print(squared_numbers)