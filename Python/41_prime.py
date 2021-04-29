# cook your dish here
p=int(input())
i=2
flag=False
while(i<p or p==1 or p==2):
    if(p==1 or p==2):
        print("prime")
        break
    elif(p%i==0):
        print("not prime")
        break
    else:
        flag=True
    i=i+1
if(flag==True):
    print("prime")