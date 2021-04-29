my_dict={
    "kartik":"a very special boy",
    "mewara":"surname",
    "rishabh":"friend",
     1:2,
     "marks":[1,2,3], #we can add list in dictionaries
     "dcti_new":{"hello":"first program"},
     "kartik":"beliver" #isme keys ke last written value hi rehti han no same keys can exist i.e no duplicate keys support in python dictionaries

}
print(my_dict)

# now we try to update out dict 
update_dict={
    "new":"exclusive",
    "btc":"bitcoin",
    "kartik":"millionaire"
}

my_dict.update(update_dict)#this adds new values as well as update the existing ones and dictionaries are mutable
print(my_dict)
print(my_dict["kartik"])

print(list(my_dict.keys())) #print only keys
print(my_dict.values())
print(my_dict.items())

print(my_dict.get("kartik"))
print(my_dict["kartik"])

# the main difference between .get and [] is that .get never give error but []give error when keys dont match as .get gives none
print(my_dict.get("karti"))
# print(my_dict["karti"])

