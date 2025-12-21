
#Numbers in Python are immutable, meaning that once a number is created, it cannot be changed.
#Integer (int): Whole numbers, positive or negative, without decimals. 
# In Python 3, integers have unlimited precision.
sagarChocolates = 10
print(f"Initial id of sagarChocolates: {id(sagarChocolates)}")
sagarChocolates = 15
print(f"Id after changing sagarChocolates :{id(sagarChocolates)}")

# Demonstrating Addition 

num1 = 7
num2 = 3
sum_result = num1 + num2
print(f"Sum of {num1} and {num2} is: {sum_result}")

# Demonstrating Subtraction
sub_result = num1-num2
print(f"Subtraction of {num1} and {num2} is : {sub_result}")

# Finding the type of an integer
x = 10
print (f"Type of x is {type(x)}")