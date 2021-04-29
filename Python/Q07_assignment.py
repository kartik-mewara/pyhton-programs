dct={
    "hello":"world",
    "kartik":"Mewara",
}
a=input("enter the key to find if already exist\n")
n=dct.get(a)
if(n!=None):
    print("The key entered is already exist and its value is:",n)
else:
    print("Key does not exist")