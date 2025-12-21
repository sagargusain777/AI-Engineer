#Strings (str) in Python are sequences of characters used to store text. 
# Just like the integers you tested earlier, strings are immutable—once you create them, 
# you cannot change the characters inside them in place.

name = 'Sagar'
print(f"Initial id of name: {id(name)}")
# Attempting to change the first character of the string (this will raise an error) 
# name[0] = 's'  # Uncommenting this line will raise a TypeError

knowledge = "GeeksforGeeks"
print(f"First character:{knowledge[0]}")
print(f"Type of knowledge is {type(knowledge)}")
print(f"Last Character: {knowledge[12]}")


#Accesing characters in a string using indexing
greeting = "Hello,World!"
print(f"First character of greeting: {greeting[0]}")  # Output: H
print(f"Seventh character of greeting: {greeting[6]}")  # Output: W

#Accessing characters using negative indexing
print(f"Last character of greeting: {greeting[-1]}")  # Output: !
print(f"Second last character of greeting: {greeting[-2]}")  # Output: d