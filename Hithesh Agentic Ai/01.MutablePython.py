#A mutable object can be changed after it is created. You can add, remove, or 
# modify its contents without creating a new object or changing its memory address (identity).

spices = set()
print("Initial id of spices:", id(spices))
# Adding elements to the set
spices.add("salt")
print("id after adding salt:", id(spices))
print ("Spices after adding salt:", spices)
spices.add("pepper")
print("id after adding pepper:", id(spices))

spices.add("cinnamon")
print("id after adding cinnamon:", id(spices))
print ("Spices after adding cinnamon:", spices)