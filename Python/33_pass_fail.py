a=int(input("Enter marks of subject a\n"))
b=int(input("Enter marks of subject b\n"))
c=int(input("Enter marks of subject c\n"))
d=int(input("Enter out of\n"))

if((a/d)*100>=33):
    a=(a/d)*100
    if((b/d)*100>=33):
        b=(b/d)*100
        if((c/d)*100>=33):
            c=(c/d)*100
            if((a+b+c)/3>=40):
                print("PASS")
            else:
                print("FAIL")
        else:
            print("FAIL")   
    else:
        print("FAIL")
else:
    print("FAIL")