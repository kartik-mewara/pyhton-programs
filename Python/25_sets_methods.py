s={1,2,3,4,5,6}
print(s)
print(type(s))
s1={}
print(type(s1)) #this will result in type of dict so for making empty set we follow given method
s1=set()
print(type(s1))
s1.add(10)
s1.add(20)
print(s1)
s1.add((1,2,3))
# s1.add([1,2,3]) this will throws an erros as we can only add types which are hashable of unmutable as list is unhashable
# s1.add({1:2}) same goes for dictionary
# set is datatype which is collection of unrepeated values 
print(s1)
s1.add(20)
s1.add(20)
print(s1)
print(len(s1)) #gives tghe lenght of the set
s1.remove(10)
print(s1)
a=s1.pop() #it removes the random item and it return it 
print(s1)
print(a)
s1.clear() # it clears the full set
print(s1)