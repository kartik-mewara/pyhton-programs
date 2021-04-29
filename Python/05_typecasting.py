# a="1234"
# a+=5
# print(a) this will not work as a is a string but we expect ans 1239so for that we will type cast a which is string into int 
a="1234"
print(type(a))
a=int(a)
a+=5
print(type(a))
print(a)

# now it will work fine
#  similerly we can type cast string to int to string int to float float to in etc
b=2.3
c="2.3"
d=345
b=str(b)
# c=int(c) #here we will get error becoz in string it is float and we are trying to make it int for that we need to make it first float then we will make it int
c=float(c)
print(type(c))
c=int(c)
print(type(c))
d=float(d)
print(b)
print(c)
print(d)
