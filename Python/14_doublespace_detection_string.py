a=input("Enter the some string with double spaces \n")
index=a.find("  ")
print("The double spaces occurs at the index:\n",index)
print("Now we will replace double spaces with single space")
a=a.replace("  "," ") #it is important to assign the string to itself to make things applicable or to work as other wise it wont work
print('Now the single spaced string is :"',a,'"')