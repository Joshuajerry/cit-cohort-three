# write a python program to print alphabets in uppercase from a to z
  
print("Uppercase Alphabets are:")
for i in range(65,91): 
        ''' to print alphabets with seperation of space.'''
        print(chr(i),end=' ')
        
        
import string
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
   print(letter, end =" ")



# write a python program to print alphabets in lowercase from a to z
  
print("\nLowercase Alphabets are:")
for j in range(97,123): 
        print(chr(j),end=' ')