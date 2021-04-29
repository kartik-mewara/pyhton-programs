def great_three(n1,n2,n3):
    if(n1>n2 and n1>3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n2 and n3>n1):
        return n3

n1=3
n2=4
n3=9

gt=great_three(n1,n2,n3)
print(f"greatest among {n1,n2,n3} is:{gt}")