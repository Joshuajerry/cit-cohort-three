# # CIT Python Quiz Week 4

# 1. Create a 2-D array and slice out the second number in the second column
import email
import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
print(a)
b = a[0:2, 0:3]
print(b)



# 2. Write a python program to sort array element in the ascending/descending order
nums = [1, 5, 3, 4, 2, 10, 6, 8, 7, 9]
nums.sort()
print('List in Ascending Order: ', nums)

nums.sort(reverse=True)
print('List in Descending Order: ', nums)



# 3. Write a python program to find the maximum and minimum value in a given 2-D array

myArray = [[8,2,3,4,5,6],[3,6,6,7,2,6],[3,8,5,1,2,9],[6,4,2,7,8,3]]
mymin = min([min(r) for r in myArray])



# 4.  Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
#     - percentage less than `50` (Grade C)
#     - percentage equal to `50` and less than `80` (Grade B)
#     - percentage equal to `80` and more than `80` (Grade A)

math = float(input("Enter the Math marks here: "))
sst = float(input("Enter the SST marks here: "))
science = float(input("Enter the Science marks here: "))
pe = float(input("Enter the PE marks here: "))
english = float(input("Enter the English marks here: "))

total = math + sst + science + pe + english
average = total / 5
percentage = (total / 500) * 100

if percentage >= 80:
    grade = 'A'
    
elif percentage >= 50:
    grade = 'B'

elif percentage < 50:
    grade = 'c'
    
print(f'Total marks = {total}')
print(f'Marks percentage = {percentage}')
print(f'Grade = {grade}')



# 5. Write a python program to fetch only Email ID from text file  which include following fields -:
#     - Name
#     - Mobile Number
#     - Roll Number
#     - Email ID
import re
fname = input("Enter the filename: ")
try:
    fhand = open(fname)
    for line in fhand:
        line = line.strip()
        gmail = re.findall(re.findall('[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+', line))
        if (len(gmail) > 0):
            print(gmail)
except:
    print("File not found")


# 6. Write a function for checking the speed of drivers.
# This function should have one parameter: speed.
#     - If speed is less than 70, it should print “Ok”.
#     - Otherwise, for every 5km above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
#     - If the driver gets more than 12 points, the function should print:“`License suspended`”
points = 2
speed = int(input("Enter the car speed: "))

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
print(check_speed(speed))

# 7. Write a function called `show_stars(rows)`. If rows is 5, it should print the following:
# ```bash
# *
# **
# ***
# ****
# *****
# ```

def show_stars(rows):
    for i in range(0, rows):
        # nested loop for each column
        for j in range(0, i + 1):
            # print star
            print("*", end=' ')
        # new line after each row
        print("\r")
        
print(show_stars(5))

	
# 8. Write a program which will find all such 
# numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

for num in range(2000,3200):
    if num % 7 == 0 and num % 5 != 0:
        print(num,",",end="")


# 9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:

# ```bash
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# ```
values = input("Enter some numbers:\n").split(",")
#This is the list
print(values)
#This is the tuple
print(tuple(values))



# 10. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# `100,150,180`
# The output of the program should be:
# `18,22,24`
import math

numbers = input("Input D: ")
numbers = numbers.split(',')

result = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result.append(Q)

print(result)


# 11. Write a function to compute 5/0 and use try/except to catch the exceptions.
def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')

# 13. Bonus Question: Algorithm challenge: Create your own sorting algorithm.

def bubblesort(list):
# Swap the elements to arrange in order
   for iter_num in range(len(list)-1, 0, -1):
      for indx in range(iter_num):
         if list[indx] > list[indx+1]:
            temp = list[indx]
            list[indx] = list[indx + 1]
            list[indx + 1] = temp
            
            
list = [19,2,31,45,6,11,121,27]
print(bubblesort(list))
print(list)