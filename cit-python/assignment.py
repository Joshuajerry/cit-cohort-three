# my_name = "Alunga Joshua Jerry"
# age = 21
# weight = 5

# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# # using formatted strings
# print(f"My name is {my_name}, i am {age} years and i weigh {weight}kgs")

numbers = [12,75,150,180,145,525,50]
newList = []

for num in numbers:
    while num % 5 == 0:
        if num <= 150:
            continue
        elif num < 500:
            break
        else:
            newList.append(num)
            print(newList)
    print(newList)