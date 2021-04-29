a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
c=int(input("Enter the third number\n"))
d=int(input("Enter the fourth number\n"))

if(a>b and a>c and a>d):
    print("a is greatest and value is:",a)
elif(b>a and b>c and b>d):
    print("b is greatest and value is:",b)
elif(c>a and c>b and c>d):
    print("c is greatest and value is:",c)
elif(d>a and d>c and d>b):
    print("d is greatest and value is:",d)