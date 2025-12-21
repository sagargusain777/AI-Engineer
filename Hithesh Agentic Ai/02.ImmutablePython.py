#An immutable object cannot be changed once it is created.
#  If you try to modify it, Python will actually create a completely new object 
# in memory and point your variable to that new object.

sagarAge = 25
print("Initial id of sagarAge:", id(sagarAge))
# Modifying the integer value
sagarAge += 1
print("id after incrementing sagarAge:", id(sagarAge))
print("sagarAge after incrementing:", sagarAge)