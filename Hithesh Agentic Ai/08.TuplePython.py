#Tuple is a built-in data structure used to store an ordered collection of items.
#Immutable: This is the defining feature. You cannot modify elements after creation.
#Ordered: Items have a defined order, and that order will not change.
#Indexed: You can access items using an index (starting at 0), just like a list.
#Allow Duplicates: Tuples can contain multiple occurrences of the same value.
#Heterogeneous: They can hold data of different types (integers, strings, lists, etc.).

my_tuple = (1, "Hello", 3.14)
print(my_tuple)
# Using String
tup = ('Geeks', 'For')
print(tup)


#Acessing Tuple Elements
#You can access tuple elements using indexing and slicing, similar to lists.

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])    # Output: 10
print(my_tuple[1:4])  # Output: (20, 30, 40)

colors = ("red", "green", "blue")
print(colors[1])
print(colors[0])    # Output: red
print(colors[-1])   # Output: blue (negative indexing)
print(colors[0:2])  # Output: ('red', 'green') (slicing)

