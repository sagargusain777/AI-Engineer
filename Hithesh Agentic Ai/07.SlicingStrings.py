
#Slicing in Python

my_string = "Awesome Agentic AI"

print(f"Original String: {my_string}")
print(f"sliced String :{my_string[0:7]}") # Slicing from index 0 to 6

print(f"Complete String using slicing: {my_string[0:]}") # Slicing the complete string

print(f"Slicing with step value: {my_string[0:17:2]}") # Slicing with step value of 2


#Reversing a string using slicing

myName = "Sagar Gusain"

reversed_name = myName[::-1]
print(f"Reversed String: {reversed_name}")