#Unpacking in Tuple
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Value of x: {x}")
print(f"Value of y: {y}")
print(f"Value of z: {z}")

spices = ("Salt", "Pepper", "Cumin", "Turmeric", "Chili Powder")
first_spice, second_spice, third_spice , fourth_spice , fifth_spice = spices

print(f"First Spice: {first_spice}")
print(f"Second Spice: {second_spice}")

 #Concatenation of Tuples   
tuple1 = (1, 2, 3)
tuple2 = ('sagar', 'hitesh','dhruv')
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)

#Slicing in Tuple
geektuples = tuple("GeeksforGeeks")
print(geektuples[0:5])  # Output: ('G', 'e', 'e', 'k', 's')
print(geektuples[5:])   # Output: ('f', 'o', 'r', 'G', 'e', 'e', 'k', 's')
print(geektuples[::-1])