# 1. Write a Python program to sum all the items in a list.
#     - The list should be generated using list comprehension
#     - The size of the list should be from a user input

size = int(input("size of the list to sum up: "))
gen_list = []
sum = 0

for i in range(1,size + 1): 
  gen_list.append(i)
  sum += i
  
print(sum)
  

# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : `['abc', 'xyz', 'aba', '1221']`

sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0

for word in sample_list:
    if len(sample_list) > 1 and sample_list[0] == sample_list[-1]:
        count += 1
        
print(count)



# 3. Write a Python program to remove duplicates from a list, given list
#     `fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]`

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
final_list = []

for word in fruits:
    if word not in final_list:
        final_list.append(word)

print(final_list)



# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
unwanted = [0, 4, 5]

# Though indexes of elements in known,deleting the elements randomly will change the values of indexes.
# Hence, it is always recommended to delete the largest indices first.
# Using this strategy, index of smaller values will not be changed.
# We can sort the list in reverse order and delete the elements of list in descending order.
for color in sorted(unwanted, reverse = True):
    del sample[color]
    
print (sample)



# 5. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
square_list = []

for i in range(1,31): 
  square_list.append(i*i) 
 
del square_list[0:5]
print(*square_list)