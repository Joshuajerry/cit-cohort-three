# Program to add natural
# numbers up to nth term

# sequence: sum = 1 + 2 + 3 + ... + n

# initialize sum and counter
sum = 0
counter = 1

n = int(input("Enter the value of n: "))

# calculate sum of first n natural numbers
while counter <= n:
    sum = sum + counter
    counter = counter + 1

# display the sum
print("The sum is", sum)


'''Example to demonstrate the use of else in while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Use of break statement inside the loop

for val in "Python":
    if val == "h":
        break
    print(val)
    
    
# Use of continue statement inside the loop

for val in "Python":
    if val == "h":
        continue
    print(val)