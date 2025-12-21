#Integer in Boolean
x = 5
print(f"X is {bool(x)}")    # Output: True because any non-zero integer is considered True

y=0
print(f"Y is {bool(y)}")    # Output: False because zero is considered False

#Float in Boolean
pi=3.14
print(f"Pi is {bool(pi)}")   # Output: True because any non-zero float is considered True
zeroFloat=0.0
print(f"Zero Float is {bool(zeroFloat)}")  # Output: False because zero float is considered False

#Negative Integer in Boolean
negInt=-10
print(f"Negative Integer is {bool(negInt)}")  # Output: True because any non-zero integer is considered True
negZeroInt=-0   
print(f"Negative Zero Integer is {bool(negZeroInt)}")  # Output: False because zero is considered False