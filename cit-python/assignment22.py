# print first 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i, end = '  ')
    i += 1


# sum of all numbers from 1 to a given number
n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of numbers is: ", sum)


# write a program to print the multiplication table of a given number
number = int(
    input("Enter the number of which you want to print the multiplication table: "))
# We are using "for loop" to iterate the multiplication 10 times
print("The Multiplication Table of: ", number)

for count in range(1, 11):
    print(number, 'x', count, '=', number * count)


# number is divisible by 5
# if the number is graeter than 150 then skip it and get to the next one
# if the number is greater than 500 then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
newList = []

print("done")

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
        break
# print("done")
print(newList)


# program to count the total number of digits in a number using a while loop given number is 4673453
num = 4673453
count = 0
while(num > 0):
    count = count + 1
    num = num // 10
print("The number of digits in the number are:", count)


# Display numbers from -10 to -1

start, end = -10, -1

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num < 0:
        print(num, end=" ")
