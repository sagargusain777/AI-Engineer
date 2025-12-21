#Python Boolean type is one of the built-in data types provided by Python, 
# which represents one of the two values i.e. True or False. 


a = True
b = False
print(f"Type of a is", type(a))
print(f"Type  of b is {type(b)}")

#Python Bool function

# Returns False as x is None
x = None
print(bool(x))  # Output: False
age = 18
print(bool(age))  # Output: True
avenger=[]
print(bool(avenger))  # Output: False


#Boolean values are often used in conditional statements and logical operations to control the flow of a program.
if a:
    print("a is True")  
else:
    print("a is False")