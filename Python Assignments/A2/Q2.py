#to show the difference between the two inputs
a=10
b=10

print("address:",id(a))
print("address:",id(b))

a=[10]
b=[10]

print("address:",id(a))
print(type(a))
print("address:",id(b))

# in the first 2 numbers id of both the numbers is same but below the numbers are treated as a list thats why a and b have different memory adress
