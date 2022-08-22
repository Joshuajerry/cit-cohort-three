# A program to print individual fruit in a list of fruits
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)
    
    
# print(range(10))

# print(list(range(10)))

# print(list(range(2, 8)))

# print(list(range(2, 20, 3)))


# A Program to iterate through a list using indexing

# fruits = ["apple", "banana", "cherry"]

# for i in range(len(fruits)):
#     print("Current fruit :", fruits[i])


# digits = [0, 1, 5]

# for digit in digits:
#     print(digit)
# else:
#     print("No items left.")
    
    
# program to display student's marks from record
student_name = 'Priscilla'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')